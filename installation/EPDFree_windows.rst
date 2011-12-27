Python Installation on Windows with EPDFree
===========================================

Use the Free Enthought Python Distribution (EPDFree) to install the
necesssary Python packages on Windows.  `Enthought
<http://www.enthought.com>`_ sponsors much of the development for
`NumPy`_ and `SciPy`_. EPDFree is a bundled binary distribution of
Python including a set of useful packages.

To download EPD go to the `EPDFree download
<http://enthought.com/products/epd_free.php>`_ page. Double click on
the the .msi file, and choose to install for All Users. If you are
using Vista and the installation may abort giving an error about
insufficient privileges. In this case, open a terminal as an
administrator (right click and run as administrator) and then run the
the .msi file from the terminal command line.

To check the installation has completed successfully try running
ipython by either selecting the PyLab application from the Start menu,
or typing on the command prompt::

  C:\Python27\Scripts\ipython.exe --pylab

To exit IPython enter::

  exit()

Install additional packages
---------------------------

Once you've installed EPDFree you can install the additional packages
listed in the :ref:`python_pkg_requirements` section.  Open a terminal
and copy and paste the lines below one at a time, checking that each
one works.  The program outputs may contain various "warnings", but
watch for "errors" and look at the end to see if a successful
installation was reported::

  cd C:\Python27\Scripts
  easy_install.exe --upgrade pip
  pip.exe install --upgrade distribute
  pip.exe install asciitable
  pip.exe install atpy
  pip.exe install aplpy

To install the remainder of the packages below a C-compiler is
required. Setting up a C-compiler on Windows is currently beyond the
scope of these instructions. They are not essential for the course,
however, and if you don't have a C-compiler set up you can skip them
for now::

  pip.exe install pyregion
  pip.exe install pyfits
  pip.exe install pywcs  
  pip.exe install http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  pip.exe install http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz


Test your installation
^^^^^^^^^^^^^^^^^^^^^^

To do a very basic test whether you meet the requirements and have a
functioning core scientific Python installation, do the following to
check version numbers. First on the command line check the version
numbers of python and ipython::

  python -V
  ipython --version

Then run ipython from the command line with the ``--pylab`` flag::

  ipython --pylab

and inside ipython run the following python commands::

  import numpy
  import scipy
  import scipy.linalg
  import pylab as plt

  print numpy.__version__
  print scipy.__version__
  print matplotlib.__version__

  x = numpy.linspace(0, 20, 100)
  plt.plot(x, sin(x))
  print scipy.linalg.eig([[1, 2], [3, 4]])

They should run without errors.  The version numbers should meet the
requirements and finally you should see a plot of a sine wave.

To check the other required packages, do the following also from
within ipython::

  import asciitable
  import atpy
  import aplpy
  import pyfits
  import pywcs

If all the above commands ran without errors, you've installed
everything successfully!

.. _NumPy: http://numpy.scipy.org/
.. _SciPy: http://www.scipy.org/
