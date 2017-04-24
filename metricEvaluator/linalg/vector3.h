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

#ifndef VECTOR3_H
#define VECTOR3_H

#include "vector.h"

#include <iostream>
#include <cmath>

/**
 * \brief a 3d vector
 */
template <typename X>
class DVector3 : public DVector<X>
{
  public:
    DVector3() : DVector<X>(3) {}

    //! constructor taking 3 coordinates
    DVector3(const X& x, const X& y, const X& z);
    DVector3(const DVector3<X>&);
    DVector3(const DVector<X>&);

    DVector3& operator=(const DVector<X>& );

    //! return the x coordinate
    const X& x() const { return (*this)[0];}
    //! return the y coordinate
    const X& y() const { return (*this)[1];}
    //! return the z coordinate
    const X& z() const { return (*this)[2];}
    X& x() { return (*this)[0];}
    X& y() { return (*this)[1];}
    X& z() { return (*this)[2];}

    // TODO overwrite operators to save range checks

    DVector3<X> cross(const DVector3<X>& other) const;
    
};

typedef DVector3<double> Vector3;
typedef DVector3<float>  Vector3f;
typedef DVector3<int>    IVector3;

template <class X>
DVector3<X>& DVector3<X>::operator=(const DVector<X>& m) {
  if (this == &m)
    return *this;
  if (m.size() != 3)
    throw std::runtime_error("vector size != 3");
  if (!--(*this->shares)) {
    delete [] this->elems;
    delete this->shares;
  }
  this->shares = const_cast<int*>(m.getShares());
  this->elems  = const_cast<X*>(m.getData());
  this->_size  = m.size();
  (*this->shares)++;
  return *this;
}

template <class X>
DVector3<X>::DVector3(const DVector<X>& m) : DVector<X>(m)
{
  if (m.size() != 3)
    throw std::runtime_error("vector size != 3");
}

template <class X>
DVector3<X>::DVector3(const DVector3<X>& m) : DVector<X>(m)
{
}

template <class X>
DVector3<X>::DVector3(const X& x, const X& y, const X& z) : DVector<X>(3)
{
  this->elems[0] = x;
  this->elems[1] = y;
  this->elems[2] = z;
}

template <class X>
DVector3<X> DVector3<X>::cross(const DVector3<X>& other) const
{
  return DVector3<X>(this->elems[1] * other.elems[2] - this->elems[2] * other.elems[1],
		     this->elems[2] * other.elems[0] - this->elems[0] * other.elems[2],
		     this->elems[0] * other.elems[1] - this->elems[1] * other.elems[0] );
}

#endif
