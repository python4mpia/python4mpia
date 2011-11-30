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
option** is to use the `Free Enthought Python Distribution
<http://www.enthought.com/products/epd_free.php>`_
(EPDFree). `Enthought <http://www.enthought.com>`_ sponsors much of
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
using a Mac you can install the necessary packages using Macports by
following `these instructions
<http://astrofrog.github.com/macports-python/>`_. This is one way to
get a 64-bit Python installation on a Mac, which isn't available with
EPDFree.  But if you're not sure which installation method to use it's
simplest to follow the instructions below to install EPDFree.

Installation Python and the Core Scientific packages
----------------------------------------------------

Follow the relevant link below for detailed instructions on how to
install the core Python using either EPDFree, your Linux package
manager, or MacPorts:

.. toctree::
   :maxdepth: 1
   
   EPDFree
   linux
   macports


Install additional packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you've installed the core Python along with Numpy, Scipy,
Matplotlib and IPython using one of the methods in the previous
section, you can install the additional packages listed in the
:ref:`python_pkg_requirements` section.  Copy and paste the lines
applicable to your system one at a time, checking that each one works.
The program outputs may contain various "warnings", but watch for
"errors" and look at the end to see if a successful installation was
reported.

Of these packages only ``pywcs`` was a significant issue during the
CfA Python for Astronomers series.  Most Windows users and a few MacOS
users had problems.  Since then a patch has been released, but it is
still known to fail for 32-bit Windows XP.  This package is required
to make images with ``APLpy`` and do WCS coordinate transformations,
but otherwise it is not absolutely needed.

MacOS or root linux install
############################
::

  easy_install --upgrade pip
  pip install --upgrade distribute
  pip install asciitable
  pip install pyfits
  pip install pywcs
  pip install atpy
  pip install aplpy
  pip install pyregion
  pip install pyparsing
  pip install http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  pip install http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz

Non-root linux
############################
::

  easy_install --user --upgrade pip
  pip install --user --upgrade distribute
  pip install --user asciitable
  pip install --user pyfits
  pip install --user pywcs
  pip install --user atpy
  pip install --user aplpy
  pip install --user pyregion
  pip install --user pyparsing
  pip install --user http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  pip install --user http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz

Windows
############################

For Windows XP 32-bit the following are known to have problems: pywcs,
pyregion, and coords.
::

  cd C:\Python27\Scripts
  easy_install.exe --upgrade pip
  pip.exe install --upgrade distribute
  pip.exe install asciitable
  pip.exe install pyfits
  pip.exe install pywcs     
  pip.exe install atpy
  pip.exe install aplpy
  pip.exe install pyregion  
  pip.exe install pyparsing
  pip.exe install http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  pip.exe install http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz


.. Admonition:: What is pip and easy_install and distribute and setuptools?

   Things can appear very confusing if you start installing packages
   on your own and looking through various projects and installation
   documentation.  First there was the ``distutils`` standard library
   module that specifies what a package provides and how it gets
   installed.  But this had some shortcomings and a 3rd party
   extension named ``setuptools`` was developed and adopted fairly
   widely.  In conjunction with ``setuptools`` was a script
   ``easy_install`` that took care of downloading, untarring,
   building, and installing packages.  Pretty good, except that the
   developer of both these stopped actively developing them.

   So some people took matters into their own hands and did a
   "friendly fork" of ``setuptools`` named ``distribute``. Now
   ``distribute`` is the standard, and likewise ``pip`` has replaced
   ``easy_install`` as the best (and actively developed) easy
   installer.

.. _installation_test:

Test your installation
^^^^^^^^^^^^^^^^^^^^^^^^

To do a very basic test whether you meet the requirements and have a
functioning core scientific Python installation, do the following and
check version numbers::

  % python -V
  % ipython -V
  % ipython -pylab
  import numpy
  import scipy
  import scipy.linalg

  print numpy.__version__
  print scipy.__version__
  print matplotlib.__version__

  x = numpy.linspace(0, 20, 100)
  plot(x, sin(x))
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
