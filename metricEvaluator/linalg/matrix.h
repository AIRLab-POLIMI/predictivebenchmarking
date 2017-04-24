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

#ifndef MATRIX_HXX 
#define MATRIX_HXX

#include <iostream>
#include <fstream>
#include <stdexcept>
#include <cmath>
#include <limits>

#include "vector.h"

/**
 * \brief A generic matrix template. We have typedef Matrix which uses
 * doubles and Matrixf which uses floats
 */
template <class X>
class DMatrix {
  public:
    DMatrix(int n=0,int m=0);
    ~DMatrix();
    
    /** Definition of X to be accessable from the outside (for templated classes) */
    typedef X real;

    DMatrix(const DMatrix&);
    DMatrix& operator=(const DMatrix&);

    X * operator[](int i) {
      if ((*shares)>1) detach();
      return mrows[i];
    }
    const X * operator[](int i) const { return mrows[i]; }

    /**
     * return the determinant of the matrix. Throws a runtime error, if matrix is
     * not square
     */
    X det() const;
    /**
     * return the inverse of the matrix. May throw an runtime error, if the matrix
     * is not invertable
     */
    DMatrix<X> inv() const;
    /**
     * return the transpose A^T of the Matrix A
     */
    DMatrix<X> transpose() const;

    DMatrix<X> operator*(const DMatrix<X>&) const;
    DMatrix<X> operator+(const DMatrix<X>&) const;
    DMatrix<X> operator-(const DMatrix<X>&) const;
    DMatrix<X> operator*(const X&) const;
    DMatrix<X> operator/(const X&) const;
    DMatrix<X> operator-() const;

    DMatrix<X>& operator+=(const DMatrix<X>&);
    DMatrix<X>& operator-=(const DMatrix<X>&);
    DMatrix<X>& operator*=(const X&);
    DMatrix<X>& operator/=(const X&);

    bool operator==(const DMatrix<X>& other) const;
    bool operator!=(const DMatrix<X>& other) const {return !((*this) == other);}

    template <typename Y> DVector<Y> operator*(const DVector<Y>& vec) const;

    template <typename Y, typename Z> friend DVector<Y> operator* (const DVector<Y>& vec, const DMatrix<Z>& mat);
    template <typename Y> friend DMatrix<Y> operator* (const Y& x, const DMatrix<Y>& mat);
    template <typename Y> friend DMatrix<Y> operator/ (const Y& x, const DMatrix<Y>& mat);

    operator DMatrix<float>() const;
    operator DMatrix<double>() const;
    
    //! return the number of rows
    int rows() const { return nrows; }
    //! return the number of columns
    int columns() const { return ncols; }

    //! calculate the sum of all matrix elems
    X sum() const;
    //! calculate the trace of the matrix (sum of the elems on the main diag)
    X trace() const;

    /**
     * make a deep copy of the matrix and detach it from the shared memory
     */
    void detach();

    //! Changes all values in the matrix to zero
    void makeZero();

    /**
     * create from any other dataType that supports [i][j] to access a_ij of the Matrix A
     */
    template <typename Y> static DMatrix<X> createFromMatrix(const Y& mat, int rows, int cols);
    
    //! return identity matrix of size n times n
    static DMatrix<X> I(int n);
    //! return a diag matrix with the vector elems on the diagonal
    static DMatrix<X> diag(const DVector<X>& v);
    //! return a matrix filled with ones
    static DMatrix<X> ones(int rows, int cols);
    //! return a matrix filled with zeros
    static DMatrix<X> zeros(int rows, int cols);

    const X* getElems() const {return elems;}
    const X* const * getMRows() const {return mrows;}
    const int* getShares() const {return shares;}

  protected:
    int nrows,ncols;
    X* elems;
    X** mrows;

    int* shares;
};

typedef DMatrix<double> Matrix;
typedef DMatrix<float> Matrixf;

template <class X> DMatrix<X>::DMatrix(int n,int m) {
  if (n<0) n=0;
  if (m<0) m=0;
  nrows=n;
  ncols=m;
  elems=new X[nrows*ncols];
  mrows=new X* [nrows];
  for (int i=0;i<nrows;i++) mrows[i]=elems+ncols*i;
  for (int i=0;i<nrows*ncols;i++) elems[i]=X(0);
  shares=new int;
  (*shares)=1;
}

template <class X> DMatrix<X>::~DMatrix() {
  if (--(*shares)) return;
  delete [] elems;
  delete [] mrows;
  delete shares;
}

template <class X> DMatrix<X>::DMatrix(const DMatrix& m) {
  shares=m.shares;
  elems=m.elems;
  nrows=m.nrows;
  ncols=m.ncols;
  mrows=m.mrows;
  (*shares)++;
}

template <class X>
DMatrix<X>& DMatrix<X>::operator=(const DMatrix& m) {
  if (this == &m)
    return *this;
  if (!--(*shares)) {
    delete [] elems;
    delete [] mrows;
    delete shares;
  }
  shares=m.shares;
  elems=m.elems;
  nrows=m.nrows;
  ncols=m.ncols;
  mrows=m.mrows;
  (*shares)++;
  return *this;
}

template <class X>
DMatrix<X> DMatrix<X>::inv() const
{
  if (nrows!=ncols) throw std::runtime_error("DMatrix is not square");
  DMatrix<X> aux1(*this),aux2(I(nrows));
  aux1.detach();
  for (int i=0;i<nrows;i++) {
    int k=i;
    for (;k<nrows&&aux1.mrows[k][i]==X(0); k++) ;
    if (k>=nrows) throw std::runtime_error("DMatrix is not invertible");
    X val=aux1.mrows[k][i];
    for (int j=0;j<nrows;j++) {
      aux1.mrows[k][j]=aux1.mrows[k][j]/val;
      aux2.mrows[k][j]=aux2.mrows[k][j]/val;
    }
    if (k!=i) {
      for (int j=0;j<nrows;j++) {
        X tmp=aux1.mrows[k][j];
        aux1.mrows[k][j]=aux1.mrows[i][j];
        aux1.mrows[i][j]=tmp;
        tmp=aux2.mrows[k][j];
        aux2.mrows[k][j]=aux2.mrows[i][j];
        aux2.mrows[i][j]=tmp;
      }
    }
    for (int j=0;j<nrows;j++)
      if (j!=i) {
        X tmp=aux1.mrows[j][i];
        for (int l=0;l<nrows;l++) {
          aux1.mrows[j][l]=aux1.mrows[j][l]-tmp*aux1.mrows[i][l];
          aux2.mrows[j][l]=aux2.mrows[j][l]-tmp*aux2.mrows[i][l];
        }
      }
  }
  return aux2;
}

template <class X>
X DMatrix<X>::det() const
{
  if (nrows!=ncols)
    throw std::runtime_error("DMatrix is not square");
  DMatrix<X> aux(*this);
  X d=X(1);
  aux.detach();
  for (int i=0;i<nrows;i++) {
    int k=i;
    for (;k<nrows&&aux.mrows[k][i]==X(0);k++) ;
    if (k>=nrows) return X(0);
    X val=aux.mrows[k][i];
    for (int j=0;j<nrows;j++) {
      aux.mrows[k][j]/=val;
    }
    d=d*val;
    if (k!=i) {
      for (int j=0;j<nrows;j++) {
        X tmp=aux.mrows[k][j];
        aux.mrows[k][j]=aux.mrows[i][j];
        aux.mrows[i][j]=tmp;
      }
      d=-d; 
    }
    for (int j=i+1;j<nrows;j++){
      X tmp=aux.mrows[j][i];
      if (!(tmp==X(0)) ){
        for (int l=0;l<nrows;l++) {
          aux.mrows[j][l]=aux.mrows[j][l]-tmp*aux.mrows[i][l];
        }
        //d=d*tmp;
      }   
    }
  }
  return d;
}

template <class X>
DMatrix<X> DMatrix<X>::transpose() const
{
  DMatrix<X> aux(ncols, nrows);
  for (int i=0; i<nrows; i++)
    for (int j=0; j<ncols; j++)
      aux[j][i]=mrows[i][j];
  return aux;
}

template <class X>
DMatrix<X> DMatrix<X>::operator*(const DMatrix<X>& m) const
{
  if (ncols!=m.nrows)
    throw std::runtime_error("Incompatible DMatrix");
  DMatrix<X> aux(nrows,m.ncols);
  for (int i=0;i<nrows;i++)
    for (int j=0;j<m.ncols;j++){
      X a=0;
      for (int k=0;k<ncols;k++)
        a+=mrows[i][k]*m.mrows[k][j];
      aux.mrows[i][j]=a;
    }
  return aux;
}

template <class X>
DMatrix<X> DMatrix<X>::operator+(const DMatrix<X>& m) const
{
  if (ncols != m.ncols || nrows != m.nrows)
    throw std::runtime_error("Incompatible DMatrix");
  DMatrix<X> aux(nrows,ncols);
  int cnt = nrows*ncols;
  for (int i = 0; i < cnt; ++i)
    aux.elems[i] = elems[i] + m.elems[i];
  return aux;
}

template <class X>
DMatrix<X> DMatrix<X>::operator-(const DMatrix<X>& m) const
{
  if (ncols!=m.ncols||nrows!=m.nrows)
    throw std::runtime_error("Incompatible DMatrix");
  DMatrix<X> aux(nrows,ncols);
  int cnt = nrows*ncols;
  for (int i = 0; i < cnt; ++i)
    aux.elems[i] = elems[i] - m.elems[i];
  return aux;
}

template <class X>
DMatrix<X> DMatrix<X>::operator*(const X& e) const
{
  DMatrix<X> aux(nrows,ncols);
  int cnt = nrows*ncols;
  for (int i = 0; i < cnt; ++i)
    aux.elems[i] = elems[i] * e;
  return aux;
}

template <class X>
DMatrix<X>& DMatrix<X>::operator+=(const DMatrix<X>& m)
{
  if (ncols != m.ncols || nrows != m.nrows)
    throw std::runtime_error("Incompatible DMatrix");
  if ((*shares)>1) detach();
  int cnt = nrows*ncols;
  X* tmpElems1 = elems;
  X* tmpElems2 = m.elems;
  for (int i = 0; i < cnt; ++i)
    *(tmpElems1++) += *(tmpElems2++);
  return *this;
}

template <class X>
DMatrix<X>& DMatrix<X>::operator-=(const DMatrix<X>& m)
{
  if (ncols!=m.ncols||nrows!=m.nrows)
    throw std::runtime_error("Incompatible DMatrix");
  if ((*shares)>1) detach();
  int cnt = nrows*ncols;
  for (int i = 0; i < cnt; ++i)
    elems[i] -= m.elems[i];
  return *this;
}

template <class X>
DMatrix<X>& DMatrix<X>::operator*=(const X& e)
{
  if ((*shares)>1) detach();
  int cnt = nrows*ncols;
  for (int i = 0; i < cnt; ++i)
    elems[i] *= e;
  return *this;
}

template <class X>
template <class Y>
DVector<Y> DMatrix<X>::operator*(const DVector<Y>& vec) const
{
  if (vec.size() != ncols)
    throw std::runtime_error("DMatrix/DVector dimensions do not agree.");

  DVector<Y> prod(nrows);
  for (int row = 0; row < nrows; row++){
    prod[row] = 0;
    for (int col = 0; col < ncols; col++)
      prod[row] += (*this)[row][col] * vec[col];
  }
  return prod;
}

template <class X>
bool DMatrix<X>::operator==(const DMatrix<X>& other) const
{
  if (ncols != other.ncols || nrows != other.nrows)
    return false;
  int cnt = ncols*nrows;
  for (int i = 0; i < cnt; ++i)
    if (elems[i] != other.elems[i])
      return false;
  return true;
}

template <class X>
void DMatrix<X>::detach()
{
  DMatrix<X> aux(nrows,ncols);
  int cnt = nrows*ncols;
  for (int i = 0; i < cnt; ++i)
    aux.elems[i] = elems[i];
  operator=(aux);
}

template <class X>
DMatrix<X> DMatrix<X>::I(int n)
{
  DMatrix<X> aux(n,n);
  for (int i = 0; i < n; ++i)
    aux[i][i]=X(1);
  return aux;
}

template <class X>
std::ostream& operator<<(std::ostream& os, const DMatrix<X> &m)
{
  os << "{";
  for (int i=0;i<m.rows();i++) {
    if (i>0) os << ",";
    os << "{";
    for (int j=0;j<m.columns();j++) {
      if (j>0) os << ", ";
      os << m[i][j];
    }
    os << "}";
  }
  os << "}";
  return os;
}

template <class X>
std::ofstream& operator<<(std::ofstream& os, const DMatrix<X> &m)
{
  for (int i=0;i<m.rows();i++) {
    if (i > 0)
      os << std::endl;
    for (int j=0;j<m.columns();j++) {
      if (j > 0)
        os << " ";
      os << m[i][j];
    }
  }
  return os;
}

template <typename Y, typename Z>
DVector<Y> operator* (const DVector<Y>& vec, const DMatrix<Z>& mat)
{
  if (vec.size() != mat.columns())
    throw std::runtime_error("DMatrix/DVector dimensions do not agree.");
  DVector<Y> prod(mat.columns());
  for (int col = 0; col < mat.columns(); col++){
    prod[col] = 0.;
    for (int row = 0; row < mat.rows(); row++)
      prod[col] += vec[row] * mat[row][col];
  }
  return prod;
}

template <typename Y>
DMatrix<Y> operator/ (const Y& x, const DMatrix<Y>& mat)
{
  DMatrix<Y> out(mat);
  for (int row = 0; row < out.rows(); row++)
    for (int col = 0; col < out.columns(); col++)
      out[row][col] = x / mat[row][col];
  return out;
}

template <typename Y>
DMatrix<Y> operator* (const Y& x, const DMatrix<Y>& mat)
{
  return mat * x;
}

template <typename X>
DMatrix<X> DMatrix<X>::operator-() const
{
  DMatrix out(nrows, ncols);
  for (int row = 0; row < nrows; ++row)
    for (int col = 0; col < ncols; ++col)
      out[row][col] = -(*this)[row][col];
  return out;
}

template <typename X>
DMatrix<X> DMatrix<X>::operator/ (const X& x) const
{
  DMatrix out(nrows, ncols);
  for (int row = 0; row < nrows; ++row)
    for (int col = 0; col < ncols; ++col)
      out[row][col] = (*this)[row][col] / x;
  return out;
}

template <typename X>
DMatrix<X>& DMatrix<X>::operator/=(const X& x)
{
  if ((*shares)>1) detach();
  for (int row = 0; row < nrows; ++row)
    for (int col = 0; col < ncols; ++col)
      mrows[row][col] /= x;
  return *this;
}

template <typename X>
DMatrix<X> DMatrix<X>::diag(const DVector<X>& v)
{
  DMatrix<X> mat(v.size(), v.size());
  for (int i = 0; i < v.size(); ++i)
    mat[i][i] = v[i];
  return mat;
}

template <typename X>
DMatrix<X> DMatrix<X>::ones(int rows, int cols)
{
  DMatrix<X> mat(rows, cols);
  for (int i = 0; i < rows; ++i)
    for (int j = 0; j < cols; ++j)
      mat[i][j] = 1;
  return mat;
}

template <typename X>
DMatrix<X> DMatrix<X>::zeros(int rows, int cols)
{
  DMatrix<X> mat(rows, cols);
  for (int i = 0; i < rows; ++i)
    for (int j = 0; j < cols; ++j)
      mat[i][j] = 0;
  return mat;
}

template <typename X>
X DMatrix<X>::sum() const
{
  X s(0);
  int cnt = nrows*ncols;
  for (int i = 0; i < cnt; ++i)
    s += elems[i];
  return s;
}

template <typename X>
X DMatrix<X>::trace() const
{
  X s(0);
  int cnt = std::min(nrows, ncols);
  for (int i = 0; i < cnt; ++i)
    s += mrows[i][i];
  return s;
}

template <class X>
template <typename Y>
DMatrix<X> DMatrix<X>::createFromMatrix(const Y& mat, int rows, int cols)
{
  DMatrix<X> aux(rows, cols);
  for (int i = 0; i < rows; ++i)
    for (int j = 0; j < cols; ++j)
      aux[i][j] = mat[i][j];
  return aux;
}

template <typename X>
void DMatrix<X>::makeZero() {
  if ((*shares)>1) detach();
  X* tmpElems = elems;
  unsigned int size = nrows*ncols;
  for (unsigned int i=0; i<size; i++)
    *(tmpElems++) = (X)0;
}

template <class X>
DMatrix<X>::operator DMatrix<float>() const {
  DMatrix<float> ret(nrows,ncols);
  for (int row=0; row<nrows; row++) {
    for (int col=0; col<ncols; col++) {
      ret[row][col] = (*this)[row][col];
    }
  }
  return ret;
}

template <class X>
DMatrix<X>::operator DMatrix<double>() const {
  DMatrix<double> ret(nrows,ncols);
  for (int row=0; row<nrows; row++) {
    for (int col=0; col<ncols; col++) {
      ret[row][col] = (*this)[row][col];
    }
  }
  return ret;
}

#endif
