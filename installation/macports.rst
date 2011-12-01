.. _MacPorts:

MacPorts
========

Why use MacPorts?
-----------------

Installing a full Python using MacPorts is very easy. The advantages of using
MacPorts over other packages are:

* A full 64-bit installation of Python
* The ability to install different Python versions side by side (e.g. 2.7 and
  3.2)
* The ability to seamlessly install a number of packages that can otherwise be
  tricky to install on Mac
* An easy mechanism for updating packages
* The ability to install many other useful non-Python utilities, including the
  GNU Fortran compilers and many common X11 applications (``xemacs``, ``gv``,
  ``xv``, etc.)

The only downside is the long wait for the initial installation (which can
take hours) since everything is compiled from source. But this can be left
overnight for example, and does not require continuous attention.

The following instructions here are adapted from `here
<http://astrofrog.github.com/macports-python/>`_

Installing MacPorts
-------------------

Ensure that `XCode <http://developer.apple.com/xcode/>`_ 3 or 4 is installed
(should be on the install DVDs for your Mac). If you like to live on the
bleeding edge, you can purchase XCode 4 from the Mac App Store. To check if
XCode is installed properly, you can type ``gcc`` in the command-line. If you
get ``gcc: command not found``, then XCode is not properly installed.

Download the DMG image for MacPorts from `here <http://www.macports.org/install.php>`_ - be sure to pick the correct
one for your MacOS X version. Mount the disk image and run the installer.

.. note:: if needed, it is possible to install MacPorts without root/admin
          privileges - see `here
          <https://trac.macports.org/wiki/InstallingMacPorts#InstallMacPortsfromsourceasanunprivilegednon-rootuser>`_
          for more details.

Installing Packages
-------------------

Go to the terminal and update the package index::

    sudo port selfupdate

To install Python and most of the basic Python packages, run::

    sudo port install py27-matplotlib py27-numpy py27-scipy py27-ipython py27-pip

Note that this will probably take several hours, and is best done overnight.

To install the packages required for this course, use::

    sudo port install py27-pyfits py27-pywcs py27-vo py27-asciitable py27-atpy py27-aplpy

MacPorts will automatically take care of any dependencies, including
``py27-pyregion`` and ``py27-parsing``.

.. note:: by default SQL dependencies are not installed for ``py27-atpy``, and 
          the Montage dependency is not installed for ``py27-aplpy``. If you
          want to install these, use sudo port install ``py27-atpy +sql``) and
          sudo port install ``py27-aplpy +montage respectively``).

Configuration
-------------

If it does not already exist, create a folder called ``.matplotlib`` in your
home directory and copy the default ``matplotlibrc`` file to it::

    cp /opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/matplotlib/mpl-data/matplotlibrc ~/.matplotlib/

Edit .matplotlib/matplotlibrc and change the following line::

    backend : Agg

to::

    backend : MacOSX

This ensures that when you use Matplotlib interactively, a window will pop up.
Optionally, you can uncomment and set the image.origin and image.interpolation
lines to::

    image.origin : lower
    image.interpolation : nearest

These settings are likely to be the most useful for plotting astronomical
data.

Make this Python installation the default::

    sudo port select --set python python27
    sudo port select --set ipython ipython27

Note that this is optional - you can also invoke this Python installation by
using ``python2.7`` and ``ipython-2.7``.

Searching for packages
----------------------

To check if a package is available through MacPorts, you can do::

    $ port search pyfits

    py25-pyfits @2.4.0 (python, science)
    Python interface to FITS formatted files

    py26-pyfits @2.4.0 (python, science)
    Python interface to FITS formatted files

    py27-pyfits @2.4.0 (python, science)
    Python interface to FITS formatted files

    Found 3 ports.

Be sure to install the one for the correct Python version (``py27-*`` if
you've been using the above instructions).

Before installing the package, you can check what variants are available::

    $ port variants py27-aplpy
    py27-aplpy has the variants:
    [+]avm: Include support for AVM meta-data
    [+]ds9: Include support for DS9 region files
      montage: Include support for Montage reprojection
    [+]rgb: Include support for RGB images
      universal: Build for multiple architectures
      
Variants listed with ``[+]`` are installed by default. To remove a default
variant, use ``-variant``. To include a variant not installed by default, use
``+variant``. For example, the following will install APLpy with support for
Montage, but not for RGB images::

    sudo port install py27-aplpy +montage -rgb
    
Installing packages not in MacPorts
-----------------------------------

.. warning:: Do not use ``sudo`` when installing packages not in MacPorts!  
             Read the following instructions carefully to avoid any issues.

When installing packages not in MacPorts, first make sure that you remove your
``.pydistutils`` file if you have one, then simply use::

    python setup.py install --user

(do not omit ``--user`` and do not use ``sudo``). This will place user
installed packages in ``~/Library/Python/2.7/lib/python/site-packages`` where
they will automatically be picked up by the Python installation, without
messing up the MacPorts file structure. Note that you can also install
packages in a similar way using ``easy_install-2.7`` and ``pip-2.7`` by
specifying the ``--user`` option.

The reason for installing packages with ``--user`` is that if instead you
install packages using ``sudo python setup.py install``, the packages will be
installed inside the MacPorts tree, but MacPorts won't be aware of it, so this
could cause issues in future if the package is installed via MacPorts. As a
rule of thumb, don't ever install anything into ``/opt/local/`` other than via
the port command. If you did mistakenly install packages to the MacPorts
directory, just go to
``/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages``
and remove the files relating to the package you installed.

