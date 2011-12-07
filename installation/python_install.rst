:tocdepth: 2

.. _`installing_scientific_python`:

Installing a scientific Python distribution
===========================================

In order to run the examples to be presented in the workshops, your
Python installation will need to meet the
:ref:`python_pkg_requirements`.  Unless you are confident with (and
enjoy) tracking down compiler errors and other issues related to
package incompatibilities, we strongly recommend using a pre-built
binary Python distribution.  For MacOS in particular there are a whole
slew of options for Python which don't play well together.  Even if
you already have an installation on your system you will probably save
time in the long run by starting fresh with a binary Python
distribution.

For Windows, MacOS and linux non-root installation, **the easiest
option** is to use the Free Enthought Python Distribution (EPDFree).

.. toctree::
   :maxdepth: 1
   
   EPDFree installation instructions (MacOS, Linux and Windows) <EPDFree> 

`Enthought <http://www.enthought.com>`_ sponsors much of
the development for `NumPy`_ and `SciPy`_. EPDFree is a bundled binary
distribution of Python including a set of useful packages. For the
Python for Astronomers workshop series held at the Harvard Center for
Astrophysics in 2011, over 50 astronomers successfully installed and
used EPD on a variety of platforms (including Windows).


**Alternatives to EPDFree**

If you have a Linux distribution and have root access to your
computer, you can instead install the necessary packages using your
default package manager (for example, ``apt-get`` or the Software
Centre on Ubuntu, or ``yum`` on Fedora).  Alternatively, if you are
using a Mac you can install the necessary packages using
Macports. This is one way to get a 64-bit Python installation on a
Mac, which isn't available with EPDFree.  But if you're not sure which
installation method to use it's simplest to follow the instructions
below to install EPDFree.

.. toctree::
   :maxdepth: 1

   Linux package manager installation instructions <linux>
   Macports installation instructions <macports>

.. _test_your_installation:

Test your installation
^^^^^^^^^^^^^^^^^^^^^^^^

To do a very basic test whether you meet the requirements and have a
functioning core scientific Python installation, do the following to
check version numbers. First on the command line check the version
numbers of python and ipython::

  python -V
  ipython -V

Then run ipython with the ``-pylab flag``::

  ipython -pylab

and run the following python commands::

  import numpy
  import scipy
  import scipy.linalg
  import pylab as plt

  print numpy.__version__
  print scipy.__version__
  print matplotlib.__version__

  x = numpy.linspace(0, 20, 100)
  plt.plot(x, sin(x))
  print scipy.linalg.eig([[1,2],[3,4]])

The commands above should succeed with no errors.  The version numbers
should meet the requirements, and finally you should see a plot of a
sine wave.

To check the other required packages, do the following from within
ipython::

  import asciitable
  import pyfits
  import pywcs
  import atpy
  import aplpy

.. include:: ../references.rst
