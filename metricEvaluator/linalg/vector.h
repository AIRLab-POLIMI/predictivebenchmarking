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

#ifndef VECTOR_HXX
#define VECTOR_HXX

#include <iostream>
#include <fstream>
#include <cmath>
#include <stdexcept>

/**
 * \brief A generic vector class. Vector uses doubles and Vectorf floats
 */
template <class X>
class DVector
{
  public:
    /** default constructor */
    DVector();
    /** constructor which takes the dimension of the vector */
    explicit DVector(int n);
    ~DVector();

    /** Definition of X to be accessable from the outside (for templated classes) */
    typedef X real;

    DVector(const DVector&);
    DVector& operator=(const DVector&);

    X& operator[](int i) {
      if ((*shares)>1) detach();
      return elems[i];
    }
    const X& operator[](int i) const { return elems[i]; }

    DVector<X> operator+(const DVector&) const;
    DVector<X> operator-(const DVector&) const;

    inline void minus(const DVector<X>& v, DVector<X>& result) const;
    inline void plus(const DVector<X>& v, DVector<X>& result) const;
    inline void times(const X& e, DVector<X>& result) const;

    DVector<X> operator-() const;
    X operator*(const DVector<real>& other) const;
    DVector<X> operator*(const X&) const;
    DVector<X> operator/(const X&) const;
    template <typename Y> friend DVector<Y> operator* (double x, DVector<Y> const &v);
    template <typename Y> friend DVector<Y> operator/ (double x, DVector<Y> const &v);

    DVector<X>& operator+=(const DVector<X>& v);
    DVector<X>& operator-=(const DVector<X>& v);
    DVector<X>& operator*=(const X& x);
    DVector<X>& operator/=(const X& x);

    bool operator==(const DVector<X>& other) const;
    bool operator!=(const DVector<X>& other) const {return !((*this) == other);}

    operator DVector<float>() const;
    operator DVector<double>() const;
    
    //! return the size of the vector
    int size() const { return _size;}
    //! return the size of the vector
    int dim() const { return _size;}

    //! return maximium value of the vector
    X max() const;
    //! return minimum value of the vector
    X min() const;
    //! return index of the max elem
    int argMax() const;
    //! return index of the min elem
    int argMin() const;
    //! return absolute max value
    X absMax() const;
    //! return absolute min value
    X absMin() const;
    //! return the sum of the vector elems
    X sum() const;
    //! squared norm of the vector
    X normSqr() const;
    //! norm of the vector
    X norm() const;
  
    //! unify the vector and return the unit vector
    DVector<X>& unit();
    //! calculate the dot product with the Vector v
    X dot(const DVector<X>& v) const;
    /**
     * stack the other vector at the end of this vector
     */
    DVector<X> stack(const DVector<X>& other) const;

    template <typename Y> static DVector<X> createFromVector(const Y& vec, int size);

    //! return a n-dimensional 1
    static DVector<X> ones(int n);
    //! return a n-dimensional 0
    static DVector<X> zeros(int n);

    void detach();

    const X* getData() const {return elems;}
    const int* getShares() const {return shares;}

    /**
     * Sets the subvector of this at the given position to the given vector
     */
    void setSubvector(unsigned int pos, const DVector<X>& v);
    /**
     * Adds the subvector of this at the given position to the given vector
     */
    void addSubvector(unsigned int pos, const DVector<X>& v);
    /**
     * extract a sub vector from this vector, starting at the given pose and using the given len (number of elements to copy
     */
    DVector<X> getSubVector(unsigned int pos, unsigned int len);

    //! Changes all values in the vector to zero
    void makeZero();

    /** Write to file */
    void saveBinary(std::ofstream &file) const;
    /** Read from file */
    void readBinary(std::ifstream &file);
 
    
  protected:
    int _size;
    X* elems;

    int* shares;
};

typedef DVector<double> Vector;
typedef DVector<float>  Vectorf;

template <class X>
DVector<X>::DVector()
{
  _size = 0;
  elems = new X[_size];
  for (int i=0; i < _size; ++i)
    elems[i] = X(0);
  shares=new int;
  (*shares)=1;
}

template <class X>
DVector<X>::DVector(int n)
{
  if (n<0) n=0;
  _size = n;
  elems = new X[_size];
  for (int i=0; i < _size; ++i)
    elems[i] = X(0);
  shares=new int;
  (*shares)=1;
}

template <class X>
DVector<X>::~DVector()
{
  if (--(*shares))
    return;
  delete [] elems;
  delete shares;
}

template <class X>
DVector<X>::DVector(const DVector& m)
{
  shares = m.shares;
  elems  = m.elems;
  _size  = m._size;
  (*shares)++;
}

template <class X>
inline DVector<X>& DVector<X>::operator=(const DVector& m) {
  if (this == &m)
    return *this;
  if (!--(*shares)) {
    delete [] elems;
    delete shares;
  }
  shares=m.shares;
  elems=m.elems;
  _size = m._size;
  (*shares)++;
  return *this;
}

template <class X>
inline DVector<X> DVector<X>::operator+(const DVector<X>& v) const
{
  if (_size != v._size)
    throw std::runtime_error("Incompatible vector size");
  DVector<X> aux(_size);
  for (int i=0; i < _size; ++i)
    aux.elems[i] = elems[i] + v.elems[i];
  return aux;
}

template <class X>
inline DVector<X> DVector<X>::operator-() const
{
  DVector<X> aux(_size);
  for (int i = 0; i < _size; ++i)
    aux.elems[i] = -elems[i];
  return aux;
}

template <class X>
inline DVector<X> DVector<X>::operator-(const DVector<X>& v) const
{
  if (_size != v._size)
    throw std::runtime_error("Incompatible vector size");
  DVector<X> aux(_size);
  for (int i = 0; i < _size; ++i)
    aux.elems[i] = elems[i] - v.elems[i];
  return aux;
}

template <class X>
inline void DVector<X>::minus(const DVector<X>& v, DVector<X>& result) const
{
  if (*result.shares > 1) result.detach();
  X* tmpElems1 = elems;
  X* tmpElems2 = v.elems;
  X* tmpElems3 = result.elems;
  
  for (int i = 0; i < _size; ++i)
    *(tmpElems3++) = *(tmpElems1++) - *(tmpElems2++);
}

template <class X>
inline void DVector<X>::plus(const DVector<X>& v, DVector<X>& result) const
{
  if (*result.shares > 1) result.detach();
  X* tmpElems1 = elems;
  X* tmpElems2 = v.elems;
  X* tmpElems3 = result.elems;
  
  for (int i = 0; i < _size; ++i)
    *(tmpElems3++) = *(tmpElems1++) + *(tmpElems2++);
}

template <class X>
inline X DVector<X>::operator*(const DVector<X>& v) const
{
  X aux = 0;
  for (int i = 0; i < _size; ++i)
    aux += elems[i] * v[i];
  return aux;
}

template <class X>
inline DVector<X> DVector<X>::operator*(const X& e) const
{
  DVector<X> aux(_size);
  for (int i = 0; i < _size; ++i)
    aux.elems[i] = elems[i] * e;
  return aux;
}

template <class X>
inline void DVector<X>::times(const X& e, DVector<X>& result) const
{
  if (*result.shares > 1) result.detach();
  X* tmpElems1 = elems;
  X* tmpElems2 = result.elems;
  
  for (int i = 0; i < _size; ++i)
    *(tmpElems2++) = e * (*(tmpElems1++));
}

template <class X>
inline DVector<X> DVector<X>::operator/(const X& e) const
{
  const X s = 1.0 / e;
  DVector<X> aux(_size);
  for (int i = 0; i < _size; ++i)
    aux.elems[i] = s * elems[i];
  return aux;
}

template <class X>
inline DVector<X>& DVector<X>::operator+=(const DVector<X>& v)
{
  if (_size != v._size)
    throw std::runtime_error("Incompatible vector size");
  if ((*shares)>1) detach();
  X* tmpElems = elems;
  X* tmpElems2 = v.elems;
  for (int i=0; i < _size; ++i)
    *(tmpElems++) += *(tmpElems2++);
  return *this;
}

template <class X>
inline DVector<X>& DVector<X>::operator-=(const DVector<X>& v)
{
  if (_size != v._size)
    throw std::runtime_error("Incompatible vector size");
  if ((*shares)>1) detach();
  X* tmpElems = elems;
  X* tmpElems2 = v.elems;
  for (int i = 0; i < _size; ++i)
    *(tmpElems++) -= *(tmpElems2++);
  return *this;
}

template <class X>
inline DVector<X>& DVector<X>::operator*=(const X& e)
{
  if ((*shares)>1) detach();
  X* tmpElems = elems;
  for (int i = 0; i < _size; ++i)
    *(tmpElems++) *= e;
  return *this;
}

template <class X>
inline DVector<X>& DVector<X>::operator/=(const X& e)
{
  if ((*shares)>1) detach();
  const X s = 1.0 / e;
  X* tmpElems = elems;
  for (int i = 0; i < _size; ++i)
    *(tmpElems++) *= s;
  return *this;
}

template <class X>
void DVector<X>::detach()
{
  DVector<X> aux(_size);
  for (int i = 0; i < _size; ++i)
    aux.elems[i] = elems[i];
  operator=(aux);
}

template <class X>
std::ostream& operator<<(std::ostream& os, const DVector<X> &m)
{
  os << "{";
  for (int i = 0; i < m.size(); ++i) {
    if (i > 0)
      os << ", ";
    os << m[i];
  }
  os << "}";
  return os;
}

template <class X>
std::ofstream& operator<<(std::ofstream& os, const DVector<X> &m)
{
  for (int i = 0; i < m.size(); ++i) {
    if (i > 0)
      os << std::endl;
    os << m[i];
  }
  return os;
}

template <typename X>
inline DVector<X> operator* (double x, DVector<X> const &v)
{
  return  v * x;
}

template <class X>
inline DVector<X> operator/ (double x, DVector<X> const &v)
{
  DVector<X> aux(v._size);
  for (int i = 0; i < v._size; ++i)
    aux.elems[i] = x / v.elems[i];
  return aux;
}


template <class X>
inline X DVector<X>::max() const
{
  X v = elems[0];
  for (int i = 1; i < _size; ++i) {
    if (elems[i] > v)
      v = elems[i];
  }
  return v;
}

template <class X>
inline X DVector<X>::min() const
{
  X v = elems[0];
  for (int i = 1; i < _size; ++i) {
    if (elems[i] < v)
      v = elems[i];
  }
  return v;
}

template <class X>
inline int DVector<X>::argMax() const
{
  int m = 0;
  for(int i=1; i < _size; ++i)
    if(elems[i] > elems[m])
      m = i;
  return m;
}

template <class X>
inline int DVector<X>::argMin() const
{
  int m = 0;
  for(int i=1; i < _size; ++i)
    if(elems[i] < elems[m])
      m = i;
  return m;
}

template <class X>
inline X DVector<X>::absMax() const
{
  double v = fabs(elems[0]);
  for (int i = 1; i < _size; ++i) {
    if (fabs(elems[i]) > v)
      v = fabs(elems[i]);
  }
  return v;
}

template <class X>
inline X DVector<X>::absMin() const
{
  double v = fabs(elems[0]);
  for (int i = 1; i < _size; ++i) {
    if (fabs(elems[i]) < v)
      v = fabs(elems[i]);
  }
  return v;
}

template <class X>
inline X DVector<X>::sum() const
{
  X sum(0);
  for (int i = 0; i < _size; ++i)
    sum += elems[i];
  return sum;
}

template <class X>
inline X DVector<X>::normSqr() const
{
  X normSqr(0);
  for (int i = 0; i < _size; ++i)
    normSqr += elems[i]*elems[i];
  return normSqr;
}

template <class X>
inline X DVector<X>::norm() const
{
  return std::sqrt(normSqr());
}

template <class X>
inline DVector<X>& DVector<X>::unit()
{
  X len = norm();
  *this /= len;
  return *this;
}

template <class X>
DVector<X> DVector<X>::stack(const DVector<X>& other) const
{
  DVector<X> aux(_size + other._size);
  for (int i = 0; i < _size; ++i)
    aux[i] = (*this)[i];
  for (int i = 0; i < other.size(); ++i)
    aux[i+_size] = other[i];
  return aux;
}

template <class X>
inline X DVector<X>::dot(const DVector<X>& v) const
{
  if (_size != v._size)
    throw std::runtime_error("Incompatible vector size");
  X dot(0);
  for (int i = 0; i < _size; ++i)
    dot += elems[i] * v.elems[i];
  return dot;
}

template <class X>
DVector<X> DVector<X>::ones(int n)
{
  DVector<X> aux(n);
  for (int i = 0; i < aux._size; ++i)
    aux.elems[i] = (X)1;
  return aux;
}

template <class X>
DVector<X> DVector<X>::zeros(int n)
{
  DVector<X> aux(n);
  for (int i = 0; i < aux._size; ++i)
    aux.elems[i] = (X)0;
  return aux;
}

template <class X>
bool DVector<X>::operator==(const DVector<X>& other) const
{
  if (_size != other._size)
    return false;
  for (int i = 0; i < _size; ++i)
    if (elems[i] != other.elems[i])
      return false;
  return true;
}

template <class X>
template <typename Y>
DVector<X> DVector<X>::createFromVector(const Y& vec, int size)
{
  DVector<X> aux(size);
  for (int i = 0; i < size; ++i)
    aux[i] = vec[i];
  return aux;
}

template <class X>
DVector<X>::operator DVector<float>() const {
  DVector<float> ret(_size);
  for (int i=0; i<_size; i++) {
    ret[i] = elems[i];
  }
  return ret;
}

template <class X>
DVector<X>::operator DVector<double>() const {
  DVector<double> ret(_size);
  for (int i=0; i<_size; i++) {
    ret[i] = elems[i];
  }
  return ret;
}

template <typename X>
void DVector<X>::setSubvector(unsigned int pos, const DVector<X>& v)
{
  int vSize = v.size();
  if ((*shares)>1) detach();
  if (_size < (int)pos+vSize)
    throw std::runtime_error("DVector: Dimensions do not agree.");
  
  for (int i=0; i<vSize; i++)
    elems[i+pos] = v[i];
}

template <typename X>
void DVector<X>::addSubvector(unsigned int pos, const DVector<X>& v)
{
  int vSize = v.size();
  if ((*shares)>1) detach();
  if (_size < (int)pos+vSize) 
    throw std::runtime_error("DVector: Dimensions do not agree.");
  
  for (int i=0; i<vSize; i++)
    elems[i+pos] += v[i];
}

template <typename X>
DVector<X> DVector<X>::getSubVector(unsigned int pos, unsigned int len)
{
  int endPos = pos + len;
  if (_size < endPos) 
    throw std::runtime_error("DVector: Dimensions do not agree.");
  DVector<X> ret(len);
  for (int i = pos, j = 0; i < endPos; ++i, ++j)
    ret[j] = elems[i];
  return ret;
}

template <typename X>
void DVector<X>::makeZero() {
  if (*shares > 1) detach();
  X* tmpElems = elems;
  for (int i=0; i<_size; i++)
    *(tmpElems++) = (X)0;
}

template <class X>
void DVector<X>::saveBinary(std::ofstream &file) const {
  //std::cout << "Now writing a size "<<_size<<" vector to disk.\n";
  file.write((char*) &_size, sizeof(_size));
  file.write((char*) elems, _size*sizeof(*elems));
}

template <class X>
void DVector<X>::readBinary(std::ifstream &file) {
  int tmpSize;
  file.read((char*) &tmpSize, sizeof(tmpSize));
  //std::cout << "Now reading a size "<<tmpSize<<" vector from disk.\n";
  DVector<X> aux(tmpSize);
  file.read((char*) aux.elems, tmpSize*sizeof(*aux.elems));
  (*this) = aux;
}
#endif
