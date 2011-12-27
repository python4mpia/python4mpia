Linux Package Manager
=====================

Here we describe how to install all the required Python packages using
the Linux distribution package manager for Debian-based systems (such
as Ubuntu). You must have root access to use this installation method.

System install with root
------------------------

For a modern linux installation such as Ubuntu 11, the system Python
version will be 2.6 or newer and all of the required core packages are
available as package installs. The instructions below have been
developed and tested with Ubuntu 11. Corresponding packages for recent
Fedora are probably available but this has not been verified.

The benefit of using a root install via the system package manager is
that it is simple and all dependencies are managed for you.  The
downside is that the package versions tend to be older and so you
don't keep up with the latest code development.  In Ubuntu 11 the core
packages (NumPy, Matplotlib) are a little out date, but unless you are
really pushing for the latest features, the older stable versions will
work perfectly well.

First install the core packages for analysis with the following::

  sudo apt-get install python-dev
  sudo apt-get install ipython
  sudo apt-get install python-numpy
  sudo apt-get install python-scipy
  sudo apt-get install python-matplotlib
  sudo apt-get install python-setuptools
  sudo apt-get install python-pyfits

Most of the remaining packages are not available in the package
manager, so we install them using the Python package manager
``pip``. To install pip::

  sudo apt-get install python-pip

Then::

  sudo pip install --upgrade distribute [--proxy web-proxy:3128]
  sudo pip install asciitable [--proxy web-proxy:3128]
  sudo pip install pywcs [--proxy web-proxy:3128]
  sudo pip install atpy [--proxy web-proxy:3128]
  sudo pip install aplpy [--proxy web-proxy:3128]
  sudo pip install pyregion [--proxy web-proxy:3128]
  sudo pip install pyparsing [--proxy web-proxy:3128]
  sudo pip install http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz [--proxy web-proxy:3128]
  sudo pip install http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz [--proxy web-proxy:3128]

where the [--proxy web-proxy:3128] option may be required if you are
within the MPIA network.

Quick installation check 
^^^^^^^^^^^^^^^^^^^^^^^^^

Open a new terminal window and type::

  which ipython

You should see::

  /usr/bin/ipython

Install additional packages
---------------------------

Once you've installed EPDFree you can install the additional packages
listed in :ref:`python_pkg_requirements`.  Copy and paste the lines
applicable to your system one at a time, checking that each one works.
The program outputs may contain various "warnings" which can be
ignored, but watch for "errors" and look at the end to see if a
successful installation was reported.

  sudo easy_install --upgrade pip
  sudo pip install --upgrade distribute
  pip install --user asciitable
  pip install --user pyfits
  pip install --user pywcs
  pip install --user atpy
  pip install --user aplpy
  pip install --user pyregion
  pip install --user pyparsing
  pip install --user http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  pip install --user http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz


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

The commands above should succeed with no errors.  The version numbers
should meet the requirements, and finally you should see a plot of a
sine wave.

To check the other required packages, do the following also from
within ipython::

  import asciitable
  import pyfits
  import pywcs
  import atpy
  import aplpy

If all the above commands ran without errors, you've installed
everything successfully!

.. include:: ../references.rst
