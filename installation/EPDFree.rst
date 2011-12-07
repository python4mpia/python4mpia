.. _EPD_Free

EPD Free (Linux, MacOS and Windows)
=============================================================

These instructions tell you how to install all the Python packages
necessary for the course on either Linux, MacOS, or Windows using the
Free Enthought Python Distribution.

All Platforms: Download EPD
---------------------------

To download EPD go to the `EPDFree download
<http://enthought.com/products/epd_free.php>`_ page. If you are
running a Linux distribution, you need to establish whether your
computer has a 32-bit or 64-bit processor and download the relevant
package. To do this type ``uname -mpi`` at the command line.  If you
see ``x86_64 x86_64 x86_64`` you have a 64-bit machine and OS.  If you
see one or more ``i686`` or ``i386`` you are running a 32-bit OS. Only
32-bit packages are available for MacOSX and Windows installations,
but these will work on both 32-bit and 64-bit systems.

Once you've downloaded EPD, skip to the instructions below that apply
to your operating system: :ref:`Linux`, :ref:`MacOS` or :ref:`Windows`.

.. _Linux:

Linux
-----

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


Quick installation check
~~~~~~~~~~~~~~~~~~~~~~~~

Open a new terminal window and type::

  which ipython

You should see::

  /home/me/epd7.1/bin/ipython

where ``/home/me/epd7.1`` is replaced by your installation root
path. Now skip down to :ref:`install_additional_packages` to install
the remaining packages needed for the course.

.. _MacOS:

MacOS
-----

Open the EPD disk image then double-click on ``EPD.mpkg`` and follow
the prompts to install. Choose all the defaults for installing (in
particular use the default installation location).

Finally run the shell startup file, which the EPD installer has
edited::

  source ~/.profile

Quick installation check
~~~~~~~~~~~~~~~~~~~~~~~~

Open a new terminal window and type::

  which ipython

You should see something like:

  /Library/Frameworks/EPD32.framework/Versions/Current/bin/ipython

If everything has gone smoothly, skip down to
:ref:`install_additional_packages` to install the remaining packages
needed for the course.

.. _Windows:

Windows
-------

Double click on the the .msi file, and choose to install for All
Users.

Quick installation check
~~~~~~~~~~~~~~~~~~~~~~~~

Run the PyLab application from the Start menu, or from the command
prompt enter::

  C:\Python27\Scripts\ipython.exe -pylab

To exit IPython enter::

  exit()

Now skip down to :ref:`install_additional_packages` to install the
remaining packages needed for the course.


.. _install_additional_packages:

Install additional packages
---------------------------

Once you've installed EPDFree you can install the additional packages
listed in the :ref:`python_pkg_requirements` section.  Copy and paste
the lines applicable to your system one at a time, checking that each
one works.  The program outputs may contain various "warnings", but
watch for "errors" and look at the end to see if a successful
installation was reported.

Of these packages only ``pywcs`` was a significant issue during the
CfA Python for Astronomers series.  Most Windows users and a few MacOS
users had problems.  Since then a patch has been released, but it is
still known to fail for 32-bit Windows XP.  This package is required
to make images with ``APLpy`` and do WCS coordinate transformations,
but otherwise it is not absolutely needed.

Linux
~~~~~
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

Now :ref:`test_your_installation`.

MacOS
~~~~~

First ensure that XCode version 3 or 4 is installed. To check if XCode
is installed properly, type ``gcc`` on the command-line. If you get
``gcc: command not found``, then XCode is not properly installed. To
install either download it `here
<http://itunes.apple.com/us/app/xcode/id448457090?mt=12>`_, or it
should also be on the install DVDs for your Mac.

Once XCode is installed, run the following commands::

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

Now :ref:`test_your_installation`.

Windows
~~~~~~~

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


Now :ref:`test_your_installation`.


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


