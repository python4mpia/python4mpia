Linux Package Manager
=====================

Here we describe how to install all the required Python packages
using your Linux distribution's package manager. You must have root
access to use this installation method.

System install with root
------------------------

For a modern linux installation such as Ubuntu 10, the system Python
version will be 2.6 or newer and all of the required core packages are
available as package installs.  The instructions below have been
developed and tested with Ubuntu 10.  Corresponding packages for
recent Fedora are probably available but this has not been verified.
In this case you will NOT use the Enthought Python Distribution.

The benefit of using a root install via the system package manager is
that it is simple and all dependencies are managed for you.  The
downside is that the package versions tend to be older and so you
don't keep up with the latest code development.  In Ubuntu 10 the core
packages (NumPy, Matplotlib) are a year or so out of date, but unless
you are really pushing for the latest features, the older stable
versions will work perfectly well.

First install the core packages for analysis with the following::

  sudo apt-get install python-dev
  sudo apt-get install ipython
  sudo apt-get install python-numpy
  sudo apt-get install python-scipy
  sudo apt-get install python-matplotlib
  sudo apt-get install python-setuptools

Most of the remaining packages are not available in the package
manager, so we install them using ``pip``::

  sudo easy_install --upgrade pip
  sudo pip install --upgrade distribute
  sudo pip install asciitable
  sudo pip install pyfits
  sudo pip install pywcs
  sudo pip install atpy
  sudo pip install aplpy
  sudo pip install pyregion
  sudo pip install pyparsing
  sudo pip install http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  sudo pip install http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz

Quick installation check 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open a new terminal window and type::

  which ipython

You should see::

  /usr/bin/ipython


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

