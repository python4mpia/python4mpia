EPD Free (Linux)
================

To download EPD go to the `EPDFree download
<http://enthought.com/products/epd_free.php>`_ page. You need to
establish whether your computer has a 32-bit or 64-bit processor and
download the relevant package. To do this type ``uname -mpi`` at the
command line.  If you see ``x86_64 x86_64 x86_64`` you have a 64-bit
machine and operating system (OS).  If you see one or more ``i686`` or
``i386`` you are running a 32-bit OS.

Once you have downloaded the appropriate EPD package for your system,
run the installation script. For example::

   bash epd_free-7-1-2-rh5-x86.sh

Next you need to edit the appropriate shell startup file
(e.g. ``~/.cshrc``, ``~/.bash_profile``) and update your path to
include the EPD path.  For instance if you specified to install EPD in
``/home/me/epd7.1`` then the following will work::

  export PATH=/home/me/epd7.1/bin:$PATH  # bash
  set path=(/home/me/epd7.1/bin $path)   # csh or tcsh

Finally run the shell startup file with::

  source ~/.bash_profile    # bash	
  source ~/.cshrc           # csh or tcsh

To check the installation has completed successfully, open a new
terminal window and type::

  which ipython

You should see::

  /home/me/epd7.1/bin/ipython

where ``/home/me/epd7.1`` is replaced by your installation root
path.

Install additional packages
---------------------------

Once you've installed EPDFree you can install the additional packages
listed in :ref:`python_pkg_requirements`.  Copy and paste the lines
below one at a time, checking that each one works.  The program
outputs may contain various "warnings", but watch for "errors" and
look at the end to see if a successful installation was reported::

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
----------------------

To do a basic test whether you meet the requirements and have a
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
  import pyfits
  import pywcs
  import atpy
  import aplpy

If all the above commands ran without errors, you've installed
everything successfully!

.. include:: ../references.rst
