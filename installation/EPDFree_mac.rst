EPDFree Installation (MacOS)
============================

To download EPD go to the `EPDFree download
<http://enthought.com/products/epd_free.php>`_ page. Open the EPD disk
image then double-click on ``EPD.mpkg`` and follow the prompts to
install. Choose all the defaults for installing (in particular use the
default installation location).

Finally run the shell startup file, which the EPD installer has
edited::

  source ~/.profile

To check EPD has installed correctly, open a new terminal window and
type::

  which ipython

You should see something like:

  /Library/Frameworks/EPD32.framework/Versions/Current/bin/ipython

Install additional packages
---------------------------

Once you've installed EPDFree you can install the additional packages
listed in the :ref:`python_pkg_requirements` section. 

First ensure that XCode version 3 or 4 is installed. To check if XCode
is installed type ``gcc`` on the command-line. If you get ``gcc:
command not found`` then XCode is not installed. To install either
download it `here
<http://itunes.apple.com/us/app/xcode/id448457090?mt=12>`_ or use the
install DVDs for your Mac.

Once XCode is installed copy and paste the lines below one at a time,
checking that each one works. The program outputs may contain various
"warnings" that can be ignored, but watch for "errors" and look at the
end to see if a successful installation was reported::

  sudo easy_install --upgrade pip
  sudo pip install --upgrade distribute

After running these two commands close and re-open the terminal so
that ``pip`` will be recognised. Then run::

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

To do a test whether you have a functioning core scientific Python
installation, do the following to check version numbers. First on the
command line check the version numbers of python and ipython::

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

If all the above commands run without errors, you've installed
everything successfully!

.. include:: ../references.rst
