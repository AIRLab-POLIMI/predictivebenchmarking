/**********************************************************************
 *
 * This source code is part of metricEvaluator.
 *
 * metricEvaluator Copyright (c) 2009 Christian Dornhege, Bastian Steder, 
 *                    Rainer Kümmerle, Michael Ruhnke, Giorgio Grisetti, 
 *                    Cyrill Stachniss, and Alexander Kleiner
 *
 * metricEvaluator is licenced under the Common Creative License,
 * Attribution-NonCommercial-ShareAlike 3.0
 *
 * You are free:
 *   - to Share - to copy, distribute and transmit the work
 *   - to Remix - to adapt the work
 *
 * Under the following conditions:
 *
 *   - Attribution. You must attribute the work in the manner specified
 *     by the author or licensor (but not in any way that suggests that
 *     they endorse you or your use of the work).
 *  
 *   - Noncommercial. You may not use this work for commercial purposes.
 *  
 *   - Share Alike. If you alter, transform, or build upon this work,
 *     you may distribute the resulting work only under the same or
 *     similar license to this one.
 *
 * Any of the above conditions can be waived if you get permission
 * from the copyright holder.  Nothing in this license impairs or
 * restricts the author's moral rights.
 *
 * metricEvaluator is distributed in the hope that it will be
 * useful, but WITHOUT ANY WARRANTY; without even the implied 
 * warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
 **********************************************************************/

#include <iostream>
#include <deque>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <csignal>
#include <sstream>
#include <set>
#include <map>
using namespace std;
#include <getopt.h>

#include "linalg/matrix4x4.h"
#include "linalg/vectorFromString.h"
#include "statistics.h"
#include "structs.h"
#include "logutil.h"

#define DEBUG (0)
#define DEBUG_CONST (0)
#define NOTIFY_ODO_CORRECT (0)
#define DEBUG_ODO_CORRECT (0)

bool useSquaredError = false;

Matrix g_EvaluationMatrix = Matrix::I(6);

struct relation {
   double t1;
   double t2;
   Matrix4x4 c;
};

struct time_interval {
   double t1;
   double t2;
};

deque<timepos> g_OdoPoses;
deque<timepos> g_SlamPoses;
deque<relation> g_Relations;
time_interval g_OdoRange;
time_interval g_SlamRange;
time_interval g_RelationsRange;

/// for each time in g_Relations this is the odometry-corrected slam pos at the corresponding time.
map<double, point_t> g_SlamRelationPoints;

double g_MaxTimeRelationToSlam = 0.1;

struct error {
   double t1;
   double t2;
   double val;
};

class CompErrorVal
{
   public:
   bool operator()(const struct error & e1, const struct error & e2) const {
      return e1.val < e2.val;
   }
};
class CompErrorT1
{
   public:
   bool operator()(const struct error & e1, const struct error & e2) const {
      return e1.t1 < e2.t1;
   }
};
class CompErrorT2
{
   public:
   bool operator()(const struct error & e1, const struct error & e2) const {
      return e1.t2 < e2.t2;
   }
};


Matrix4x4 calcRelation(point_t p1, point_t p2)
{
   Matrix4x4 m1 = Matrix4x4::translate(p1.x, p1.y, 0) * Matrix4x4::rotZ(p1.theta);
   
   Matrix4x4 m2 = Matrix4x4::translate(p2.x, p2.y, 0) * Matrix4x4::rotZ(p2.theta);

   return m1.inv() * m2;
}

Matrix4x4 calcRelation(timepos tp1, timepos tp2)
{
   Matrix4x4 m1 = Matrix4x4::translate(tp1.pos.x, tp1.pos.y, 0) * Matrix4x4::rotZ(tp1.pos.theta);
   
   Matrix4x4 m2 = Matrix4x4::translate(tp2.pos.x, tp2.pos.y, 0) * Matrix4x4::rotZ(tp2.pos.theta);

   if(DEBUG_CONST) {
      cout << endl;
      cout << endl;
      cout << m1 << endl;
      cout << m2 << endl;
   }
   Matrix4x4 res = m1.inv() * m2;
   if(DEBUG_CONST)
      cout << res;

   return res;
}

double sqr(double x) {
   return x*x;
}

double tpDist(timepos tp1, timepos tp2)
{
   return sqrt( sqr(tp1.pos.x - tp2.pos.x) + sqr(tp1.pos.y - tp2.pos.y) );
}

void writeErrorStats(deque<error> & errors, string filename)
{
   cout << "Writing " << filename << " ... ";  fflush(stdout);

   FILE* f = fopen(filename.c_str(), "w");
   if(!f)
      return;
   for(deque<error>::iterator it = errors.begin(); it != errors.end(); it++) {
      error e = *it;
      fprintf(f, "%f\n", e.val);
   }
   fclose(f);

   cout << "done.\n";
}

deque<error> calcErrors()
{
   deque<error> errors;

   for(deque<relation>::iterator it = g_Relations.begin(); it != g_Relations.end(); it++) {
      relation c = *it;

      Matrix4x4 slamC = calcRelation(g_SlamRelationPoints[c.t1], g_SlamRelationPoints[c.t2]);
      Matrix4x4 realC = c.c;

      double sx, sy, sz, sphi, stheta, spsi;
      double rx, ry, rz, rphi, rtheta, rpsi;
      slamC.getTranslation(sx, sy, sz);
      slamC.getAngles(sphi, stheta, spsi);
      realC.getTranslation(rx, ry, rz);
      realC.getAngles(rphi, rtheta, rpsi);
      Vector slamCV(6);    // slam relation
      slamCV[0] = sx;
      slamCV[1] = sy;
      slamCV[2] = sz;
      slamCV[3] = sphi;
      slamCV[4] = stheta;
      slamCV[5] = spsi;
      Vector realCV(6);
      realCV[0] = rx;
      realCV[1] = ry;
      realCV[2] = rz;
      realCV[3] = rphi;
      realCV[4] = rtheta;
      realCV[5] = rpsi;

      Vector delta = slamCV - realCV;
      // noramlize angular errors
      delta[3] = normalize_theta(delta[3]);
      delta[4] = normalize_theta(delta[4]);
      delta[5] = normalize_theta(delta[5]);

      double value = delta.dot(g_EvaluationMatrix * delta);
      if(!useSquaredError) {
         value = sqrt(value);
      }

      error e;
      e.val = value;
      e.t1 = c.t1;
      e.t2 = c.t2;
      errors.push_back(e);
   }

   return errors;
}

void evaluate(deque<error> & errors, string errorFile)
{
   Statistics<double> stats("Error");

   for(deque<error>::iterator it = errors.begin(); it != errors.end(); it++) {
      error e = *it;

      stats.addMeasurement(e.val);
   }

   stats.print();

   if(!errorFile.empty()) {
      FILE* f = fopen(errorFile.c_str(), "w");
      fprintf(f, "Mean, Std, Min, Max, NumMeasures\n");
      fprintf(f, "%f, %f, %f, %f, %d\n", stats.getMean(), stats.getStandardDeviation(), stats.getMin(), stats.getMax(), stats.getNumMeasurements());
      fclose(f);
   }
}

/// Finds the best point for SLAM near ts
point_t calcSlamRelationPoint(double ts)
{
   // 1st search nearest point to ts in g_SlamPoses
   double nearest = HUGE_VAL;
   point_t nearestPoint;
   double nearestTs = 0;

   for(deque<timepos>::iterator it = g_SlamPoses.begin(); it != g_SlamPoses.end(); it++) {
      timepos tp = *it;
      if(fabs(tp.timestamp - ts) < nearest) {
         nearest = fabs(tp.timestamp - ts);
         nearestPoint = tp.pos;
         nearestTs = tp.timestamp;
      }
   }

   if(nearest <= g_MaxTimeRelationToSlam) {
      return nearestPoint;
   }

   if(nearest > 10000) {
      fprintf(stderr, "WARNING nearest Slam Pose to ts: %f is at %f (delta: %f) - are you using incompatible timestamps?\n", ts, nearestTs, nearest);
   }
   if(nearest > 1.0) {
      if(ts > g_SlamRange.t2) {
         fprintf(stderr, "WARNING trying to correct %f to match relation %f, but %f is already last (%f) of the slam poses.\n", nearestTs, ts, ts, g_SlamRange.t2);
      }
      if(ts < g_SlamRange.t1) {
         fprintf(stderr, "WARNING trying to correct %f to match relation %f, but %f is before first (%f) of the slam poses.\n", nearestTs, ts, ts, g_SlamRange.t1);
      }
   }

   if(g_OdoPoses.empty()) {
      fprintf(stderr, "WARNING couldnt find near enough (delta %f) slam pose to %f and no odo provided.\n", nearest, ts);
      return nearestPoint;
   }

   if(NOTIFY_ODO_CORRECT)
      printf("correcting slam %f -> relation %f by odometry\n", nearestTs, ts);   //remove/debug

   // interpolate along odo
   double tsToOdo = HUGE_VAL;
   double slamToOdo = HUGE_VAL;
   point_t tsOdo;
   double tsOdoTime = 0;
   point_t slamOdo;
   double slamOdoTime = 0;
   for(deque<timepos>::iterator it = g_OdoPoses.begin(); it != g_OdoPoses.end(); it++) {
      timepos tp = *it;
      if(fabs(tp.timestamp - ts) < tsToOdo) {
         tsToOdo = fabs(tp.timestamp - ts);
         tsOdo = tp.pos;
         tsOdoTime = tp.timestamp;
      }
      if(fabs(tp.timestamp - nearestTs) < slamToOdo) {
         slamToOdo = fabs(tp.timestamp - nearestTs);
         slamOdo = tp.pos;
         slamOdoTime = tp.timestamp;
      }
   }

   Matrix4x4 slamOdoT = Matrix4x4::translate(slamOdo.x, slamOdo.y, 0) * Matrix4x4::rotZ(slamOdo.theta);
   Matrix4x4 tsOdoT = Matrix4x4::translate(tsOdo.x, tsOdo.y, 0) * Matrix4x4::rotZ(tsOdo.theta);

   Matrix4x4 deltaOdoT = slamOdoT.inv() * tsOdoT;  // from slam pos to TS (i.e. slam pos before ts pos)

   Matrix4x4 slamPosT = Matrix4x4::translate(nearestPoint.x, nearestPoint.y, 0) * Matrix4x4::rotZ(nearestPoint.theta);

   Matrix4x4 correctedT = slamPosT * deltaOdoT;

   double x,y,z, roll,pitch,yaw;
   correctedT.getTranslation(x, y, z);
   correctedT.getAngles(roll, pitch, yaw);

   point_t corrected;
   corrected.x = x;
   corrected.y = y;
   corrected.theta = yaw;

   if(DEBUG_ODO_CORRECT) {
      cout << "\n\nRelation at " << ts << endl;
      cout << "Slam at " << nearestTs << " is (" << nearestPoint.x << ", " << nearestPoint.y << ", " << nearestPoint.theta << ")\n";
      cout << "Odo at " << slamOdoTime << " is (" << slamOdo.x << ", " << slamOdo.y << ", " << slamOdo.theta << ")\n";
      cout << "Odo at " << tsOdoTime << " is (" << tsOdo.x << ", " << tsOdo.y << ", " << tsOdo.theta << ")\n\n";
      cout << "Odo transformation at slam time " << slamOdoT << endl << slamOdoT.printable() << endl;
      cout << "Odo transformation at relation time " << tsOdoT << endl << tsOdoT.printable() << endl;;
      cout << "Delta transformation from slam pos to relation pos " << deltaOdoT << endl << deltaOdoT.printable() << endl;
      cout << "Nearest Slam transformation " << slamPosT << endl << slamPosT.printable() << endl;
      cout << "correct slam by odo transformation at relation time " << correctedT << endl << correctedT.printable() << endl;
      cout << "Final corrected pose (" << corrected.x << ", " << corrected.y << ", " << corrected.theta << endl;
   }

   return corrected;
}

void calcSlamRelations()
{
   cout << "Generating relation points from slam.\n";
   for(deque<relation>::iterator it = g_Relations.begin(); it != g_Relations.end(); it++) {
      relation c = *it;
      if(g_SlamRelationPoints.find(c.t1) == g_SlamRelationPoints.end()) {   // not in yet.
         point_t scp = calcSlamRelationPoint(c.t1);
         g_SlamRelationPoints[c.t1] = scp;
      }
      if(g_SlamRelationPoints.find(c.t2) == g_SlamRelationPoints.end()) {
         point_t scp = calcSlamRelationPoint(c.t2);
         g_SlamRelationPoints[c.t2] = scp;
      }
   }
   cout << "Done.\n\n";
}

deque<string> parseLines(FILE* fp, bool onlyCarmenLines, bool & containsOdo) 
{
   cout << "Reading log.\n";
   containsOdo = false;

   char buf[1024];

   deque<string> lines;
   string cur;

   size_t read;
   while((read = fread(buf, 1, 1024, fp)) > 0) {
      for(size_t i = 0; i < read; i++) {
         if(buf[i] != '\n') {
            cur += buf[i];
         } else {
            // only insert lines we care about
            if(!onlyCarmenLines || (cur.find("ROBOTLASER1 ") == 0) || (cur.find("ODOM ") == 0) || (cur.find("FLASER ") == 0)) {
               if(cur.find("ODOM ") == 0)
                  containsOdo = true;
               lines.push_back(cur);
            }
            cur = "";
         }
      }
   }
   if(!cur.empty())
      lines.push_back(cur);

   cout << "Done.\n\n";

   if(DEBUG) {
      for(size_t i = 0; i < min((size_t)5, lines.size()); i++) {
         cout << lines[i] << endl;
      }
      for(size_t i = lines.size() - 1; i > lines.size() - 5; i--) {
         cout << lines[i] << endl;
      }
   }

   return lines;
}

deque<string> parseLines(FILE* fp, bool onlyCarmenLines = false) 
{
   bool dummy;
   return parseLines(fp, onlyCarmenLines, dummy);
}

void parseSlam(FILE* fp)
{
   deque<string> lines = parseLines(fp, true);
   g_SlamRange.t1 = HUGE_VAL;
   g_SlamRange.t2 = -HUGE_VAL;

   cout << "Parsing Slam log.\n";
   for(deque<string>::iterator it = lines.begin(); it != lines.end(); it++) {
      string& l = *it;
      if(l.find("ROBOTLASER1 ") == 0) {
         timepos tp = parseRobotLaser(l);
         g_SlamPoses.push_back(tp);

         if(tp.timestamp < g_SlamRange.t1)
            g_SlamRange.t1 = tp.timestamp;
         if(tp.timestamp > g_SlamRange.t2)
            g_SlamRange.t2 = tp.timestamp;
      }   // does start with ROBOTLASER1
      if(l.find("FLASER ") == 0) {
         timepos tp = parseFLaser(l);
         g_SlamPoses.push_back(tp);

         if(tp.timestamp < g_SlamRange.t1)
            g_SlamRange.t1 = tp.timestamp;
         if(tp.timestamp > g_SlamRange.t2)
            g_SlamRange.t2 = tp.timestamp;
      }
   }
   cout << fixed << "Parsed messages in (" << g_SlamRange.t1 << ", " << g_SlamRange.t2 << ") = " << g_SlamRange.t2 - g_SlamRange.t1 << "s.\n\n";
}

void parseOdom(FILE* fp)
{
   bool containsOdo;
   deque<string> lines = parseLines(fp, true, containsOdo);
   g_OdoRange.t1 = HUGE_VAL;
   g_OdoRange.t2 = -HUGE_VAL;

   cout << "Parsing Odom log.\n";
   for(deque<string>::iterator it = lines.begin(); it != lines.end(); it++) {
      string& l = *it;
      if(!containsOdo) {      //HACK: look for FLASER
         static bool warned = false;
         if(!warned) {
            fprintf(stderr, "\nWARNING no odometry found in odometry log - using FLASER when possible.\n\n");
            warned = true;
         }

         timepos tp = parseFLaser(l);
         g_OdoPoses.push_back(tp);

         if(tp.timestamp < g_OdoRange.t1)
            g_OdoRange.t1 = tp.timestamp;
         if(tp.timestamp > g_OdoRange.t2)
            g_OdoRange.t2 = tp.timestamp;

         continue;
      }

      if(l.find("ODOM ") != 0)   // doesnt start with ODOM
         continue;

      timepos tp = parseOdom(l);
      g_OdoPoses.push_back(tp);

      if(tp.timestamp < g_OdoRange.t1)
         g_OdoRange.t1 = tp.timestamp;
      if(tp.timestamp > g_OdoRange.t2)
         g_OdoRange.t2 = tp.timestamp;
   }
   cout << fixed << "Parsed messages in (" << g_OdoRange.t1 << ", " << g_OdoRange.t2 << ") = " << g_OdoRange.t2 - g_OdoRange.t1 << "s.\n\n";
}

void parseRelations(FILE* fp)
{
   deque<string> lines = parseLines(fp);
   g_RelationsRange.t1 = HUGE_VAL;
   g_RelationsRange.t2 = -HUGE_VAL;

   cout << "Parsing Relations.\n";
   for(deque<string>::iterator it = lines.begin(); it != lines.end(); it++) {
      string l = *it;
      if(l.find("#") == 0)   // comment
         continue;

      relation c;
      double x, y, z, phi, theta, psi;
      sscanf(l.c_str(), "%lf %lf %lf %lf %lf %lf %lf %lf\n", &c.t1, &c.t2, &x, &y, &z, &phi, &theta, &psi);

      Matrix4x4 m = Matrix4x4::translate(x, y, z) * Matrix4x4::rot(phi, theta, psi);
      c.c = m;

      g_Relations.push_back(c);

      if(c.t1 < g_RelationsRange.t1)
         g_RelationsRange.t1 = c.t1;
      if(c.t2 < g_RelationsRange.t1)
         g_RelationsRange.t1 = c.t2;

      if(c.t1 > g_RelationsRange.t2)
         g_RelationsRange.t2 = c.t1;
      if(c.t2 > g_RelationsRange.t2)
         g_RelationsRange.t2 = c.t2;
   }
   cout << fixed << "Parsed messages in (" << g_RelationsRange.t1 << ", " << g_RelationsRange.t2 << ") = " << g_RelationsRange.t2 - g_RelationsRange.t1 << "s.\n\n";
}

void printUsage(const char* progName)
{
   cout << "Usage: " << progName << " [options]" << endl << endl;
   cout << "Options:" << endl;
   cout << "-------------------------------------------" << endl;
   cout << "-s <name>         slam log file containing ROBOTLASER1 data" << endl;   // robot_pose being true pose
   cout << "-r <relations>  the relations file" << endl;   // output format somewhere
   cout << "-o <odometry>     raw odometry log file" << endl;  // only needed if -r is not dense enough
   cout << "-w \"{wx, wy, wz, wphi, wtheta, wpsi}\"    the error weight vector (units meter/rad)" << endl;
   cout << "-q                use squared error to compute averages (instead of sqrt of squared error)" << endl;
   cout << "-e <errorfile>    write avg, std deviation, number of measurements" << endl;
   cout << "-eu <errorfile>   write list of errors (unsorted)" << endl;
   cout << "-em <errorfile>   write list of errors (sorted by magnitude)" << endl;
   cout << "-e1 <errorfile>   write list of errors (sorted by first relation timestamp)" << endl;
   cout << "-e2 <errorfile>   write list of errors (sorted by second relation timestamp)" << endl;
   cout << "-h                this help" << endl;
}

int main(int argc, char** argv)
{
   string slamFile = "";
   string odomFile = "";
   string relationFile = "";

   string errUnsortedFile = "";
   string errMagnitudeFile = "";
   string errT1File = "";
   string errT2File = "";

   string errorFile = "";

   const int OPT_ERR_UNSORTED = 256;
   const int OPT_ERR_MAGNITUDE = 257;
   const int OPT_ERR_T1 = 258;
   const int OPT_ERR_T2 = 259;

   struct option opts [] = {
      { "eu", required_argument, NULL, OPT_ERR_UNSORTED },
      { "em", required_argument, NULL, OPT_ERR_MAGNITUDE },
      { "e1", required_argument, NULL, OPT_ERR_T1 },
      { "e2", required_argument, NULL, OPT_ERR_T2 },
      { 0, 0, 0, 0 }
   };

   for (int c; (c = getopt_long_only(argc, argv, "qs:o:r:w:e:h", opts, NULL)) != EOF; ) {
      switch (c) {
         case 'q':
            useSquaredError = true;
            break;
         case 's':
            slamFile = optarg;
            break;
         case 'o':
            odomFile = optarg;
            break;
         case 'r':
            relationFile = optarg;
            break;
         case OPT_ERR_UNSORTED:
            errUnsortedFile = optarg;
            break;
         case OPT_ERR_MAGNITUDE:
            errMagnitudeFile = optarg;
            break;
         case OPT_ERR_T1:
            errT1File = optarg;
            break;
         case OPT_ERR_T2:
            errT2File = optarg;
            break;
         case 'e':
            errorFile = optarg;
            break;
         case 'w':
            {
            printf("Parsing weights: %s => ", optarg);
            Vector weights = vectorFromString(optarg);
            cout << weights << endl;
            g_EvaluationMatrix = Matrix::diag(weights);
            break;
            }
         case 'h':
            printUsage(argv[0]);
            return 0;
         default:
            printUsage(argv[0]);
            return 1;
      }
   }

   if(slamFile.empty() || relationFile.empty()) {
      printUsage(argv[0]);
      return 1;
   }

   FILE* sfp = fopen(slamFile.c_str(), "r");
   if(!sfp) {
      printf("Couldn't open %s\n", slamFile.c_str());
      return 1;
   }

   parseSlam(sfp);

   fclose(sfp);

   if(!odomFile.empty()) {
      FILE* ofp = fopen(odomFile.c_str(), "r");
      if(!ofp) {
         printf("Couldn't open %s\n", odomFile.c_str());
         return 1;
      }

      parseOdom(ofp);

      fclose(ofp);
   }

   FILE* cfp = fopen(relationFile.c_str(), "r");
   if(!cfp) {
      printf("Couldn't open %s\n", relationFile.c_str());
      return 1;
   }
   
   parseRelations(cfp);

   fclose(cfp);

   cout << "Parsed " << g_Relations.size() << " relations, " << g_SlamPoses.size() << " slam poses and " << g_OdoPoses.size() << " odometry poses.\n\n";

   if(g_SlamPoses.empty()) {
      cout << "No slam poses parsed." << endl;
      exit(1);
   }
   if(g_Relations.empty()) {
      cout << "No relations parsed." << endl;
      exit(1);
   }

   calcSlamRelations();

   deque<error> errors = calcErrors();

   if(!errUnsortedFile.empty()) {
      writeErrorStats(errors, errUnsortedFile);
   }
   if(!errMagnitudeFile.empty()) {
      sort(errors.begin(), errors.end(), CompErrorVal());
      writeErrorStats(errors, errMagnitudeFile);
   }
   if(!errT1File.empty()) {
      sort(errors.begin(), errors.end(), CompErrorT1());
      writeErrorStats(errors, errT1File);
   }
   if(!errT2File.empty()) {
      sort(errors.begin(), errors.end(), CompErrorT2());
      writeErrorStats(errors, errT2File);
   }

   evaluate(errors, errorFile);

   cout << "Finished." << endl;
   return 0;
}

