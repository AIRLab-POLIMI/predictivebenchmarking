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

#ifndef STATISTICS_H
#define STATISTICS_H

#include <math.h>
#include <stdio.h>

/// This class calculates mean and standard deviation for incremental values.
template <class T>
class Statistics
{
   public:
      Statistics(const char* name = "");
      
      void reset();
      void addMeasurement(T val);

      T getMean() const;
      T getStandardDeviation() const;
      int getNumMeasurements() const;

      T getMin() const { return _min; }
      T getMax() const { return _max; }

      void print() const;

   protected:
      T _sumMeasurements;
      T _sumSquaredMeasurements;
      double _numMeasurements;

      T _min;
      T _max;

      const char* _name;
};

template <class T>
Statistics<T>::Statistics(const char* name) : _name(name)
{
   reset();
}
      
template <class T>
void Statistics<T>::reset()
{
   _sumMeasurements = static_cast<T>(0);
   _sumSquaredMeasurements = static_cast<T>(0);
   _numMeasurements = 0;
   _min = HUGE_VAL;     // this probably only works for doubles
   _max = -HUGE_VAL;
}

template <class T>
void Statistics<T>::addMeasurement(T val)
{
   _sumMeasurements += val;
   _sumSquaredMeasurements += (val * val);
   _numMeasurements += 1.0;
   if(val > _max)
      _max = val;
   if(val < _min)
      _min = val;
}

template <class T>
T Statistics<T>::getMean() const
{
   if(_numMeasurements == 0)
      return static_cast<T>(0);
   return _sumMeasurements/_numMeasurements;
}

template <class T>
T Statistics<T>::getStandardDeviation() const
{
   if(_numMeasurements == 0)
      return static_cast<T>(0);

   return sqrt( (_numMeasurements * _sumSquaredMeasurements - _sumMeasurements * _sumMeasurements) / (_numMeasurements * (_numMeasurements - 1)) );
}

template <class T>
int Statistics<T>::getNumMeasurements() const
{
   return (int)_numMeasurements;
}

template <class T>
void Statistics<T>::print() const
{
   printf("%s: Mean %.2f Std: %.2f (Num: %.0f)\n", _name, getMean(), getStandardDeviation(), _numMeasurements);
}

#endif

