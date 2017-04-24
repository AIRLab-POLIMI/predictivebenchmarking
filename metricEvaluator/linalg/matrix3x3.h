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

#ifndef MATRIX3X3_HXX 
#define MATRIX3X3_HXX

#include <iostream>
#include <stdexcept>
#include <limits>

#include "matrix.h"
#include "vector3.h"

/**
 * \brief a derived 3x3 matrix
 */
template <class X>
class DMatrix3x3 : public DMatrix<X>
{
  public:
    DMatrix3x3() : DMatrix<X>(3, 3) {}

    DMatrix3x3(const X& m11, const X& m12, const X& m13,
        const X& m21, const X& m22, const X& m23,
        const X& m31, const X& m32, const X& m33);
    DMatrix3x3(const DMatrix3x3<X>& m);
    DMatrix3x3(const DMatrix<X>& m);

    DMatrix3x3<X>& operator=(const DMatrix<X>& m);

    X det() const;

    // TODO overwrite operators to save range checks

    //! return the 3 euler angles of the rotation matrix
    void getAngles(X &phi, X &theta, X &psi) const;

    //! set the matrix from the 3 euler angles
    void setAngles(X phi, X theta, X psi);

    //! return the rotation matrix for the 3 given euler angles phi, theta, and psi
    static DMatrix3x3<X> rot(const X& phi, const X& theta, const X& psi);
    //! return rotation matrix for a rotation around the x axis with an angle of phi
    static DMatrix3x3<X> rotX(const X& phi);
    //! return rotation matrix for a rotation around the y axis with an angle of theta
    static DMatrix3x3<X> rotY(const X& theta);
    //! return rotation matrix for a rotation around the z axis with an angle of psi
    static DMatrix3x3<X> rotZ(const X& psi);
    //! rotate with angle x around the axis (u, v, w)
    static DMatrix3x3<X> rotAngleAxis(const X& alpha, const X& u, const X& v, const X& w);
    
    /** Inverse is overwritten with closed form method for 3x3 */
    DMatrix3x3<X> inv() const;
   
};

typedef DMatrix3x3<double> Matrix3x3;
typedef DMatrix3x3<float> Matrix3x3f;

template <class X>
DMatrix3x3<X>& DMatrix3x3<X>::operator=(const DMatrix<X>& m)
{
  if (this == &m)
    return *this;
  if (m.rows() != 3 || m.columns() != 3)
    throw std::runtime_error("matrix is not 3x3");
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
DMatrix3x3<X>::DMatrix3x3(const DMatrix<X>& m) : DMatrix<X>(m)
{
  if (m.rows() != 3 || m.columns() != 3)
    throw std::runtime_error("matrix is not 3x3");
}

template <class X>
DMatrix3x3<X>::DMatrix3x3(const DMatrix3x3& m) : DMatrix<X>(m)
{
}

template <class X>
DMatrix3x3<X>::DMatrix3x3(const X& m11, const X& m12, const X& m13,
                        const X& m21, const X& m22, const X& m23,
                        const X& m31, const X& m32, const X& m33) : DMatrix<X>(3,3)
{
  (*this)[0][0] = m11; (*this)[0][1] = m12; (*this)[0][2] = m13;
  (*this)[1][0] = m21; (*this)[1][1] = m22; (*this)[1][2] = m23;
  (*this)[2][0] = m31; (*this)[2][1] = m32; (*this)[2][2] = m33;
}

template <class X>
X DMatrix3x3<X>::det() const
{
  return ((*this)[0][0] * (*this)[1][1] * (*this)[2][2] +
	  (*this)[0][1] * (*this)[1][2] * (*this)[2][0] +
	  (*this)[0][2] * (*this)[1][0] * (*this)[2][1] -
	  (*this)[0][2] * (*this)[1][1] * (*this)[2][0] -
	  (*this)[0][0] * (*this)[1][2] * (*this)[2][1] - 
	  (*this)[0][1] * (*this)[1][0] * (*this)[2][2]);
}


template <class X>
DMatrix3x3<X> DMatrix3x3<X>::rot(const X& phi, const X& theta, const X& psi)
{
  DMatrix3x3 matrix;
  matrix.setAngles(phi, theta, psi);
  return matrix;
}

template <class X>
DMatrix3x3<X> DMatrix3x3<X>::rotX(const X& ang)
{
  return DMatrix3x3( 1,         0,        0,
                     0,  cos(ang), -sin(ang),
                     0,  sin(ang),  cos(ang) );
}

template <class X>
DMatrix3x3<X> DMatrix3x3<X>::rotY(const X& ang)
{
  return DMatrix3x3( cos(ang), 0,  sin(ang),
                     0,        1,         0,
                     -sin(ang), 0,  cos(ang) );
}

template <class X>
DMatrix3x3<X> DMatrix3x3<X>::rotZ(const X& ang)
{
  return DMatrix3x3( cos(ang),-sin(ang), 0,
		    sin(ang), cos(ang), 0,
		    0,           0,     1 );
}

template <class X>
void DMatrix3x3<X>::getAngles(X &phi, X &theta, X &psi) const
{
  phi   = atan2((*this)[2][1], (*this)[2][2]);
  psi   = atan2((*this)[1][0], (*this)[0][0]);
  theta = asin(-(*this)[2][0]);
}

template <class X>
void DMatrix3x3<X>::setAngles(X phi, X theta, X psi)
{
  X A     = cos(psi),
    B     = sin(psi),
    C     = cos(theta),
    D     = sin(theta),
    E     = cos(phi),
    F     = sin(phi),
    DE    = D*E,
    DF    = D*F;
  (*this)[0][0] = A*C;
  (*this)[0][1] = A*DF - B*E;
  (*this)[0][2] = B*F + A*DE;
  (*this)[1][0] = B*C;
  (*this)[1][1] = A*E + B*DF;
  (*this)[1][2] = B*DE - A*F;
  (*this)[2][0] = -D;
  (*this)[2][1] = C*F;
  (*this)[2][2] = C*E;
}

template <class X>
DMatrix3x3<X> DMatrix3x3<X>::rotAngleAxis(const X& alpha, const X& u, const X& v, const X& w)
{
  DMatrix3x3 matrix;

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

  return matrix;
}

template <class X>
DMatrix3x3<X> DMatrix3x3<X>::inv() const {
  X determinant = det();
  if (fabs(determinant) < std::numeric_limits<X>::epsilon())
    throw std::runtime_error("DMatrix3x3 is not invertible");
  
  X detInv = 1.0 / determinant;
  return DMatrix3x3<X>(
    detInv * (this->mrows[1][1]*this->mrows[2][2] - this->mrows[1][2]*this->mrows[2][1]),
    detInv * (this->mrows[0][2]*this->mrows[2][1] - this->mrows[0][1]*this->mrows[2][2]),
    detInv * (this->mrows[0][1]*this->mrows[1][2] - this->mrows[0][2]*this->mrows[1][1]),
    detInv * (this->mrows[1][2]*this->mrows[2][0] - this->mrows[1][0]*this->mrows[2][2]),
    detInv * (this->mrows[0][0]*this->mrows[2][2] - this->mrows[0][2]*this->mrows[2][0]),
    detInv * (this->mrows[0][2]*this->mrows[1][0] - this->mrows[0][0]*this->mrows[1][2]),
    detInv * (this->mrows[1][0]*this->mrows[2][1] - this->mrows[1][1]*this->mrows[2][0]),
    detInv * (this->mrows[0][1]*this->mrows[2][0] - this->mrows[0][0]*this->mrows[2][1]),
    detInv * (this->mrows[0][0]*this->mrows[1][1] - this->mrows[0][1]*this->mrows[1][0]));
}

#endif
