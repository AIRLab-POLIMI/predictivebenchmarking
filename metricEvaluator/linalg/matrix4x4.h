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

#ifndef MATRIX4X4_HXX 
#define MATRIX4X4_HXX

#include <iostream>
#include <stdexcept>
#include <limits>
#include <string>

#include "matrix.h"
#include "matrix3x3.h"
#include "vector3.h"

/**
 * \brief a derived 4x4 matrix, e.g. used for homogeneous transformations of 3d coordinates
 */
template <class X>
class DMatrix4x4 : public DMatrix<X>
{
  public:
    DMatrix4x4() : DMatrix<X>(4, 4) {}

    DMatrix4x4(const X& m11, const X& m12, const X& m13, const X& m14,
        const X& m21, const X& m22, const X& m23, const X& m24,
        const X& m31, const X& m32, const X& m33, const X& m34,
        const X& m41, const X& m42, const X& m43, const X& m44);
    DMatrix4x4(const DMatrix4x4<X>& m);
    DMatrix4x4(const DMatrix<X>& m);

    DMatrix4x4<X>& operator=(const DMatrix<X>& m);

    /**
     * return the determinant of the matrix. Throws a runtime error, if matrix is
     * not square. Uses closed form solution for 4x4 matrices.
     */
    X det() const;
    /**
     * return the inverse of the matrix. May throw an runtime error, if the matrix
     * is not invertable. Uses closed form solution for 4x4 matrices.
     */
    DMatrix4x4<X> inv() const;

    // TODO overwrite operators to save range checks

    //! return the 3 euler angles of the rotation matrix
    void getAngles(X &phi, X &theta, X &psi) const;
    /** set the matrix elemns based on the given rotation angles */
    void setAngles(const X& phi, const X& theta, const X& psi);

    /** set all elements as in a rotX matrix */
    void setRotX(const X& phi);
    /** set all elements as in a rotY matrix */
    void setRotY(const X& theta);
    /** set all elements as in a rotZ matrix */
    void setRotZ(const X& psi);

    //! return the translation part of the matrix
    void getTranslation(X &x, X &y, X &z) const;

    //! return the translation part of the matrix
    void getTranslation(DVector3<X>& translation) const;
    //! return the translation part of the matrix
    DVector3<X> getTranslation() const { DVector3<X> ret; getTranslation(ret); return ret;}

    /** set all elems as in the translation matrix */
    void setTranslation(X x, X y, X z);

    /** set all elems as in the translation matrix */
    void setTranslation(const DVector3<X>& translation);

    /** create transformation matrix from rotation matrix and translation */
    void setTransformation(const DMatrix3x3<X>& rotation, const DVector3<X>& translation);
    
    /** create transformation matrix from Euler Angles and translation */
    void setTransformation(X x, X y, X z, X phi, X theta, X psi);
    
    //! return the rotational part of the matrix
    void getRotation(DMatrix3x3<X>& rotation) const;
    //! return the rotational part of the matrix
    DMatrix3x3<X> getRotation() const { DMatrix3x3<X> ret; getRotation(ret); return ret;}

    //! Get the inverted tranformation (=inverted rotation+translation)
    DMatrix4x4<X> invertedTransformation() const;

    //! return the rotation matrix for the 3 given euler angles phi, theta, and psi
    static DMatrix4x4<X> rot(const X& phi, const X& theta, const X& psi);
    //! return rotation matrix for a rotation around the x axis with an angle of phi
    static DMatrix4x4<X> rotX(const X& phi);
    //! return rotation matrix for a rotation around the y axis with an angle of theta
    static DMatrix4x4<X> rotY(const X& theta);
    //! return rotation matrix for a rotation around the z axis with an angle of psi
    static DMatrix4x4<X> rotZ(const X& psi);
    //! rotate with angle x around the axis (u, v, w)
    static DMatrix4x4<X> rotAngleAxis(const X& alpha, const X& u, const X& v, const X& w);

    //! translation matrix for dx, dy, dz
    static DMatrix4x4<X> translate(const X& dx, const X& dy, const X& dz);
    
    //! translation matrix for given translation
    static DMatrix4x4<X> translate(const DVector3<X>& translation);

    //! scaling matrix for sx, sy, sz
    static DMatrix4x4<X> scale(const X& sx, const X& sy, const X& sz);

    /**
     * transform the point using the 4x4 homogeneous transformation matrix
     * and return the transformed point
     */
    DVector3<X> operator() (const DVector3<X>& point) const;

    std::string printable();
};

typedef DMatrix4x4<double> Matrix4x4;
typedef DMatrix4x4<float> Matrix4x4f;

template <class X>
DMatrix4x4<X>& DMatrix4x4<X>::operator=(const DMatrix<X>& m)
{
  if (this == &m)
    return *this;
  if (m.rows() != 4 || m.columns() != 4)
    throw std::runtime_error("matrix is not 4x4");
  if (!--(*this->shares)) {
    delete [] this->elems;
    delete [] this->mrows;
    delete this->shares;
  }
  this->shares = const_cast<int*>(m.getShares());
  this->elems  = const_cast<X*>(m.getElems());
  this->nrows  = m.rows();
  this->ncols  = m.columns();
  this->mrows  = const_cast<X**>(m.getMRows());
  (*this->shares)++;
  return *this;
}

template <class X>
DMatrix4x4<X>::DMatrix4x4(const DMatrix<X>& m) : DMatrix<X>(m)
{
  if (m.rows() != 4 || m.columns() != 4)
    throw std::runtime_error("matrix is not 4x4");
}

template <class X>
DMatrix4x4<X>::DMatrix4x4(const DMatrix4x4& m) : DMatrix<X>(m)
{
}

template <class X>
DMatrix4x4<X>::DMatrix4x4(const X& m11, const X& m12, const X& m13, const X& m14,
        const X& m21, const X& m22, const X& m23, const X& m24,
        const X& m31, const X& m32, const X& m33, const X& m34,
        const X& m41, const X& m42, const X& m43, const X& m44) : DMatrix<X>(4,4)
{
  (*this)[0][0] = m11; (*this)[0][1] = m12; (*this)[0][2] = m13; (*this)[0][3] = m14;
  (*this)[1][0] = m21; (*this)[1][1] = m22; (*this)[1][2] = m23; (*this)[1][3] = m24;
  (*this)[2][0] = m31; (*this)[2][1] = m32; (*this)[2][2] = m33; (*this)[2][3] = m34;
  (*this)[3][0] = m41; (*this)[3][1] = m42; (*this)[3][2] = m43; (*this)[3][3] = m44;
}

template <class X>
X DMatrix4x4<X>::det() const
{
  X fA0 = this->elems[ 0]*this->elems[ 5] - this->elems[ 1]*this->elems[ 4];
  X fA1 = this->elems[ 0]*this->elems[ 6] - this->elems[ 2]*this->elems[ 4];
  X fA2 = this->elems[ 0]*this->elems[ 7] - this->elems[ 3]*this->elems[ 4];
  X fA3 = this->elems[ 1]*this->elems[ 6] - this->elems[ 2]*this->elems[ 5];
  X fA4 = this->elems[ 1]*this->elems[ 7] - this->elems[ 3]*this->elems[ 5];
  X fA5 = this->elems[ 2]*this->elems[ 7] - this->elems[ 3]*this->elems[ 6];
  X fB0 = this->elems[ 8]*this->elems[13] - this->elems[ 9]*this->elems[12];
  X fB1 = this->elems[ 8]*this->elems[14] - this->elems[10]*this->elems[12];
  X fB2 = this->elems[ 8]*this->elems[15] - this->elems[11]*this->elems[12];
  X fB3 = this->elems[ 9]*this->elems[14] - this->elems[10]*this->elems[13];
  X fB4 = this->elems[ 9]*this->elems[15] - this->elems[11]*this->elems[13];
  X fB5 = this->elems[10]*this->elems[15] - this->elems[11]*this->elems[14];

  X fdet = fA0*fB5-fA1*fB4+fA2*fB3+fA3*fB2-fA4*fB1+fA5*fB0;
  return fdet;
}

template <class X>
DMatrix4x4<X> DMatrix4x4<X>::inv() const
{
  // we calculate the determinat first
  // copy and paste of the det() function, since we also use the calculated
  // values in the later parts of the function
  X fA0 = this->elems[ 0]*this->elems[ 5] - this->elems[ 1]*this->elems[ 4];
  X fA1 = this->elems[ 0]*this->elems[ 6] - this->elems[ 2]*this->elems[ 4];
  X fA2 = this->elems[ 0]*this->elems[ 7] - this->elems[ 3]*this->elems[ 4];
  X fA3 = this->elems[ 1]*this->elems[ 6] - this->elems[ 2]*this->elems[ 5];
  X fA4 = this->elems[ 1]*this->elems[ 7] - this->elems[ 3]*this->elems[ 5];
  X fA5 = this->elems[ 2]*this->elems[ 7] - this->elems[ 3]*this->elems[ 6];
  X fB0 = this->elems[ 8]*this->elems[13] - this->elems[ 9]*this->elems[12];
  X fB1 = this->elems[ 8]*this->elems[14] - this->elems[10]*this->elems[12];
  X fB2 = this->elems[ 8]*this->elems[15] - this->elems[11]*this->elems[12];
  X fB3 = this->elems[ 9]*this->elems[14] - this->elems[10]*this->elems[13];
  X fB4 = this->elems[ 9]*this->elems[15] - this->elems[11]*this->elems[13];
  X fB5 = this->elems[10]*this->elems[15] - this->elems[11]*this->elems[14];

  X fDet = fA0*fB5 - fA1*fB4 + fA2*fB3 + fA3*fB2 - fA4*fB1 + fA5*fB0;
  if (fabs(fDet) <= std::numeric_limits<X>::epsilon()) {
    throw std::runtime_error("DMatrix4x4 is not invertible");
  }

  X fInvDet = ((X)1.0)/fDet;
  DMatrix4x4<X> kInv;
  kInv.elems[ 0] = fInvDet * (+ this->elems[ 5]*fB5 - this->elems[ 6]*fB4 + this->elems[ 7]*fB3);
  kInv.elems[ 4] = fInvDet * (- this->elems[ 4]*fB5 + this->elems[ 6]*fB2 - this->elems[ 7]*fB1);
  kInv.elems[ 8] = fInvDet * (+ this->elems[ 4]*fB4 - this->elems[ 5]*fB2 + this->elems[ 7]*fB0);
  kInv.elems[12] = fInvDet * (- this->elems[ 4]*fB3 + this->elems[ 5]*fB1 - this->elems[ 6]*fB0);
  kInv.elems[ 1] = fInvDet * (- this->elems[ 1]*fB5 + this->elems[ 2]*fB4 - this->elems[ 3]*fB3);
  kInv.elems[ 5] = fInvDet * (+ this->elems[ 0]*fB5 - this->elems[ 2]*fB2 + this->elems[ 3]*fB1);
  kInv.elems[ 9] = fInvDet * (- this->elems[ 0]*fB4 + this->elems[ 1]*fB2 - this->elems[ 3]*fB0);
  kInv.elems[13] = fInvDet * (+ this->elems[ 0]*fB3 - this->elems[ 1]*fB1 + this->elems[ 2]*fB0);
  kInv.elems[ 2] = fInvDet * (+ this->elems[13]*fA5 - this->elems[14]*fA4 + this->elems[15]*fA3);
  kInv.elems[ 6] = fInvDet * (- this->elems[12]*fA5 + this->elems[14]*fA2 - this->elems[15]*fA1);
  kInv.elems[10] = fInvDet * (+ this->elems[12]*fA4 - this->elems[13]*fA2 + this->elems[15]*fA0);
  kInv.elems[14] = fInvDet * (- this->elems[12]*fA3 + this->elems[13]*fA1 - this->elems[14]*fA0);
  kInv.elems[ 3] = fInvDet * (- this->elems[ 9]*fA5 + this->elems[10]*fA4 - this->elems[11]*fA3);
  kInv.elems[ 7] = fInvDet * (+ this->elems[ 8]*fA5 - this->elems[10]*fA2 + this->elems[11]*fA1);
  kInv.elems[11] = fInvDet * (- this->elems[ 8]*fA4 + this->elems[ 9]*fA2 - this->elems[11]*fA0);
  kInv.elems[15] = fInvDet * (+ this->elems[ 8]*fA3 - this->elems[ 9]*fA1 + this->elems[10]*fA0);

  return kInv;
}

template <class X>
DMatrix4x4<X> DMatrix4x4<X>::rot(const X& phi, const X& theta, const X& psi)
{
  DMatrix4x4<X> matrix;
  matrix.setAngles(phi, theta, psi);
  return matrix;
}

template <class X>
void DMatrix4x4<X>::setAngles(const X& phi, const X& theta, const X& psi)
{
  setTransformation(0, 0, 0, phi, theta, psi);
}

template <class X>
DMatrix4x4<X> DMatrix4x4<X>::rotX(const X& ang)
{
  return DMatrix4x4( 1,         0,         0, 0,
                     0,  cos(ang), -sin(ang), 0,
                     0,  sin(ang),  cos(ang), 0,
                     0,         0,         0, 1);
}

template <class X>
DMatrix4x4<X> DMatrix4x4<X>::rotY(const X& ang)
{
  return DMatrix4x4( cos(ang),  0,  sin(ang), 0,
                     0,         1,         0, 0,
                     -sin(ang), 0,  cos(ang), 0,
                     0,         0,         0, 1);
}

template <class X>
DMatrix4x4<X> DMatrix4x4<X>::rotZ(const X& ang)
{
  return DMatrix4x4( cos(ang),-sin(ang), 0, 0, 
		     sin(ang), cos(ang), 0, 0,
		            0,        0, 1, 0,
                            0,        0, 0, 1);
}

template <class X>
void DMatrix4x4<X>::getAngles(X &phi, X &theta, X &psi) const
{
  phi   = atan2((*this)[2][1], (*this)[2][2]);
  psi   = atan2((*this)[1][0], (*this)[0][0]);
  theta = asin(-(*this)[2][0]);
}

template <class X>
void DMatrix4x4<X>::getTranslation(X &x, X &y, X &z) const
{
  x = (*this)[0][3];
  y = (*this)[1][3];
  z = (*this)[2][3];
}

template <class X>
void DMatrix4x4<X>::getTranslation(DVector3<X>& translation) const
{
  translation[0] = (*this)[0][3];
  translation[1] = (*this)[1][3];
  translation[2] = (*this)[2][3];
}

template <class X>
void DMatrix4x4<X>::getRotation(DMatrix3x3<X>& rotation) const
{
  rotation[0][0] = (*this)[0][0];
  rotation[0][1] = (*this)[0][1];
  rotation[0][2] = (*this)[0][2];
  rotation[1][0] = (*this)[1][0];
  rotation[1][1] = (*this)[1][1];
  rotation[1][2] = (*this)[1][2];
  rotation[2][0] = (*this)[2][0];
  rotation[2][1] = (*this)[2][1];
  rotation[2][2] = (*this)[2][2];
}

template <class X>
DMatrix4x4<X> DMatrix4x4<X>::rotAngleAxis(const X& alpha, const X& u, const X& v, const X& w)
{
  DMatrix4x4 matrix;

  X rcos = cos(alpha);
  X rsin = sin(alpha);
  matrix[0][0] =      rcos + u*u*(1-rcos);
  matrix[1][0] =  w * rsin + v*u*(1-rcos);
  matrix[2][0] = -v * rsin + w*u*(1-rcos);
  matrix[0][1] = -w * rsin + u*v*(1-rcos);
  matrix[1][1] =      rcos + v*v*(1-rcos);
  matrix[2][1] =  u * rsin + w*v*(1-rcos);
  matrix[0][2] =  v * rsin + u*w*(1-rcos);
  matrix[1][2] = -u * rsin + v*w*(1-rcos);
  matrix[2][2] =      rcos + w*w*(1-rcos);
  matrix[3][3] = 1;

  return matrix;
}

template <class X>
DMatrix4x4<X> DMatrix4x4<X>::translate(const X& dx, const X& dy, const X& dz)
{
  return DMatrix4x4( 1, 0, 0, dx,
                     0, 1, 0, dy,
                     0, 0, 1, dz,
                     0, 0, 0, 1);
}

template <class X>
DMatrix4x4<X> DMatrix4x4<X>::translate(const DVector3<X>& translation)
{
  return DMatrix4x4( 1, 0, 0, translation[0],
                     0, 1, 0, translation[1],
                     0, 0, 1, translation[2],
                     0, 0, 0, 1);
}

template <class X>
DMatrix4x4<X> DMatrix4x4<X>::scale(const X& sx, const X& sy, const X& sz)
{
  return DMatrix4x4( sx, 0,  0, 0,
                     0, sy,  0, 0,
                     0,  0, sz, 0,
                     0,  0,  0, 1);
}

template <class X>
inline DVector3<X> DMatrix4x4<X>::operator() (const DVector3<X>& p) const
{
  X x = (*this)[0][0] * p[0] + (*this)[0][1] * p[1] + (*this)[0][2] * p[2] + (*this)[0][3];
  X y = (*this)[1][0] * p[0] + (*this)[1][1] * p[1] + (*this)[1][2] * p[2] + (*this)[1][3];
  X z = (*this)[2][0] * p[0] + (*this)[2][1] * p[1] + (*this)[2][2] * p[2] + (*this)[2][3];
  X w = (*this)[3][0] * p[0] + (*this)[3][1] * p[1] + (*this)[3][2] * p[2] + (*this)[3][3];
  return DVector3<X>(x/w, y/w, z/w);
}

template <class X>
void DMatrix4x4<X>::setRotX(const X& phi)
{
  X c = cos(phi);
  X s = sin(phi);
  (*this)[0][0] = 1; (*this)[0][1] = 0; (*this)[0][2] =  0; (*this)[0][3] = 0;
  (*this)[1][0] = 0; (*this)[1][1] = c; (*this)[1][2] = -s; (*this)[1][3] = 0;
  (*this)[2][0] = 0; (*this)[2][1] = s; (*this)[2][2] =  c; (*this)[2][3] = 0;
  (*this)[3][0] = 0; (*this)[3][1] = 0; (*this)[3][2] =  0; (*this)[3][3] = 1;
}

template <class X>
void DMatrix4x4<X>::setRotY(const X& theta)
{
  X c = cos(theta);
  X s = sin(theta);
  (*this)[0][0] = c;  (*this)[0][1] = 0; (*this)[0][2] = s; (*this)[0][3] = 0;
  (*this)[1][0] = 0;  (*this)[1][1] = 1; (*this)[1][2] = 0; (*this)[1][3] = 0;
  (*this)[2][0] = -s; (*this)[2][1] = 0; (*this)[2][2] = c; (*this)[2][3] = 0;
  (*this)[3][0] = 0;  (*this)[3][1] = 0; (*this)[3][2] = 0; (*this)[3][3] = 1;
}

template <class X>
void DMatrix4x4<X>::setRotZ(const X& psi)
{
  X c = cos(psi);
  X s = sin(psi);
  (*this)[0][0] = c; (*this)[0][1] = -s; (*this)[0][2] = 0; (*this)[0][3] = 0;
  (*this)[1][0] = s; (*this)[1][1] =  c; (*this)[1][2] = 0; (*this)[1][3] = 0;
  (*this)[2][0] = 0; (*this)[2][1] =  0; (*this)[2][2] = 1; (*this)[2][3] = 0;
  (*this)[3][0] = 0; (*this)[3][1] =  0; (*this)[3][2] = 0; (*this)[3][3] = 1;
}
template <class X>
void DMatrix4x4<X>::setTranslation(X x, X y, X z)
{
  (*this)[0][0] = 1.0; (*this)[0][1] = 0.0; (*this)[0][2] = 0.0; (*this)[0][3] = x;
  (*this)[1][0] = 0.0; (*this)[1][1] = 1.0; (*this)[1][2] = 0.0; (*this)[1][3] = y;
  (*this)[2][0] = 0.0; (*this)[2][1] = 0.0; (*this)[2][2] = 1.0; (*this)[2][3] = z;
  (*this)[3][0] = 0.0; (*this)[3][1] = 0.0; (*this)[3][2] = 0.0; (*this)[3][3] = 1.0;
}

template <class X>
void DMatrix4x4<X>::setTranslation(const DVector3<X>& translation)
{
  setTranslation(translation[0], translation[1], translation[2]);
}

template <class X>
void DMatrix4x4<X>::setTransformation(const DMatrix3x3<X>& rotation, const DVector3<X>& translation)
{
  (*this)[0][0] = rotation[0][0]; (*this)[0][1] = rotation[0][1]; (*this)[0][2] = rotation[0][2]; (*this)[0][3] = translation[0];
  (*this)[1][0] = rotation[1][0]; (*this)[1][1] = rotation[1][1]; (*this)[1][2] = rotation[1][2]; (*this)[1][3] = translation[1];
  (*this)[2][0] = rotation[2][0]; (*this)[2][1] = rotation[2][1]; (*this)[2][2] = rotation[2][2]; (*this)[2][3] = translation[2];
  (*this)[3][0] = 0.0;            (*this)[3][1] = 0.0;            (*this)[3][2] = 0.0;            (*this)[3][3] = 1.0;
}

template <class X>
void DMatrix4x4<X>::setTransformation(X x, X y, X z, X phi, X theta, X psi)
{
  X A = cos(psi),  B = sin(psi),  C = cos(theta),  D = sin(theta),
    E = cos(phi),  F = sin(phi), DE = D*E,        DF = D*F;
  (*this)[0][0] = A*C;  (*this)[0][1] = A*DF - B*E;  (*this)[0][2] = B*F + A*DE;  (*this)[0][3] = x;
  (*this)[1][0] = B*C;  (*this)[1][1] = A*E + B*DF;  (*this)[1][2] = B*DE - A*F;  (*this)[1][3] = y;
  (*this)[2][0] = -D;   (*this)[2][1] = C*F;         (*this)[2][2] = C*E;         (*this)[2][3] = z;
  (*this)[3][0] = 0;    (*this)[3][1] = 0;           (*this)[3][2] = 0;           (*this)[3][3] = 1;
}

template <class X>
DMatrix4x4<X> DMatrix4x4<X>::invertedTransformation() const
{
  return DMatrix4x4<X>((*this)[0][0], (*this)[1][0], (*this)[2][0], -(*this)[0][0]*(*this)[0][3] - (*this)[1][0]*(*this)[1][3] - (*this)[2][0]*(*this)[2][3],
                       (*this)[0][1], (*this)[1][1], (*this)[2][1], -(*this)[0][1]*(*this)[0][3] - (*this)[1][1]*(*this)[1][3] - (*this)[2][1]*(*this)[2][3],
                       (*this)[0][2], (*this)[1][2], (*this)[2][2], -(*this)[0][2]*(*this)[0][3] - (*this)[1][2]*(*this)[1][3] - (*this)[2][2]*(*this)[2][3],
                       0.0,           0.0,           0.0,           1.0);
}

template <class X>
std::string DMatrix4x4<X>::printable()
{
   X x,y,z;
   X roll,pitch,yaw;
   getTranslation(x, y, z);
   getAngles(roll, pitch, yaw);
   
   std::stringstream ss;
   ss << "{" << x << ", " << y << ", " << z << ", " << roll << ", " << pitch << ", " << yaw << "}";
   return ss.str();
}

#endif
