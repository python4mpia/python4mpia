Linux Package Manager
=====================

Here we describe how to install the core scientific Python packages
using your Linux distribution's package manager. You must have root
access to use this installation method.

System install with root
------------------------

For a modern linux installation such as Ubuntu 11, the system Python version
will be 2.6 or newer and all of the required core packages are available as 
package installs.  The instructions below have been developed and tested with
Ubuntu 11.  Corresponding packages for recent Fedora are probably available but
this has not been verified.  In this case you will NOT use the Enthought Python
Distribution.

The benefit of using a root install via the system package manager is
that it is simple and all dependencies are managed for you.  The
downside is that the package versions tend to be older and so you
don't keep up with the latest code development.  In Ubuntu 11 the core
packages (NumPy, Matplotlib) are a year or so out of date.  Unless you
are really pushing for the latest features, the older stable versions
will work perfectly well.

Install the core packages for analysis with the following::

  sudo apt-get install python-dev
  sudo apt-get install ipython
  sudo apt-get install python-numpy
  sudo apt-get install python-scipy
  sudo apt-get install python-matplotlib
  sudo apt-get install python-setuptools

Quick installation check 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open a new terminal window and type::

  which ipython

You should see::

  /usr/bin/ipython

.. _linux_nonroot:
