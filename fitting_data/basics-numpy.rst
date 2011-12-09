.. include:: ../references.rst

Basics of Numpy
=========================



The `NumPy`_ package primarily enhances the standard python arrays. However, it not only provides a more fancy interface for your arrays, it also makes the actual internal computations faster.

Again, let us consider three simple examples. But again, note that these three examples by no means exploit the wealth of functionality of Numpy!



Operations on lists
---------------

Say you have a list of 5 elements and you want to make a new list with all those 5 elements exponentiated. Wihtout Numpy, you have to iterate through this whole list by hand. Looks like this::

  import math
  
  D = [1.0,2.0,3.0,4.0,5.0]  # Define toy data.
  # Exponentiate data without Numpy.
  E = []
  for n in range(len(D)):
      E.append(math.exp(D[n]))

Thanks to Numpy, this can be done more easily::

  import numpy
  
  D = numpy.array([1.0,2.0,3.0,4.0,5.0])  # Define toy data.
  # Exponentiate data using Numpy.
  E = numpy.exp(D)

The code becomes more readible because it is shorter and omits nasty details.

*BEWARE: "exp" is defined in both packages math and Numpy. Therefore, never write something like "from math import *" because this may generate conflicts which later may cause bugs that are hard to track down.*




Linear algebra
---------------

Matrix operations are not exactly the most favourite amusement of astronomers. In fact, many of us try to avoid it as much as possible. However, if you are not afraid of it, linear algebra can do a lot for you!

First, Numpy allows you to initialise matrices of desired dimensionality::

  import numpy
  
  rows    = 3  # Number of matrix rows
  columns = 2  # Number of matrix columns
  matrix  = numpy.zeros([rows,columns])  # Generate a 3x2 matrix with zero elements

Second, Numpy provides us with the standard matrix product::

  import numpy
  
  matrix_1 = numpy.zeros([3,2])  # Generate a 3x2 matrix with zero elements
  matrix_2 = numpy.zeros([2,4])  # Generate a 2x4 matrix with zero elements
  product  = numpy.dot(matrix_1, matrix_2)  # Product of both is a 3x4 matrix

More complex functionality - such as determinants or matrix inversion - are part of the linalg-subpackage of Numpy::

  import numpy
  
  I = numpy.identity(3)  # Generate 3x3 identity matrix
  # Print determinant
  print numpy.linalg.det(I)
  # Compute inverse
  I_inv = numpy.linalg.inv(I)

Linalg provides many more functions, e.g., for eigensystems, singular-value decomposition, Cholesky decomposition, etc. You name it! If you need them, you find them in the `linalg documentation <http://docs.scipy.org/doc/numpy/reference/routines.linalg.html>`_.




Fourier transforms
---------------

Fourier transforms are also common in astronomy. For instance, due to the convolution theorem, which states that the convolution of two functions in real space is equivalent to a simple multiplication of their Fourier transforms. Convolutions appear quite often, e.g., the line-spread-function when fitting spectral lines or the point-spread-function when fitting galaxy shapes.

Now, if we first forward Fourier transform an array and then apply the inverse Fourier transform, we should be left with the initial array::

  import numpy

  # Step 1: Draw array of 10 random numbers from uniform distribution -10 to 10
  A = numpy.random.uniform(-10.0,10.0, 10)
  # Step 2: Compute fast Fourier transform.
  FT = numpy.fft.fft(A)
  # Step 3: Compute inverse FFT.
  IFT = numpy.fft.ifft(FT)
  # Step 4: Check whether results equals input.
  print IFT - A

Apart from some numerical left-overs, the result should be fine.

For more information, see the `fft documentation <http://docs.scipy.org/doc/numpy/reference/routines.fft.html>`_.