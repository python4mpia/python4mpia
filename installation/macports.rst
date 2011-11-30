.. _MacPorts:

MacPorts
========




MacOS X Developer Tools
~~~~~~~~~~~~~~~~~~~~~~~

Before you install additional packages, you will need to make sure that you
have installed the MacOS X Developer Tools (XCode) so that the ``gcc``
compiler is available. If you are not sure if you have the developer tools
installed, try typing ``gcc`` in a Terminal. You should see something like this::

    $ gcc
    i686-apple-darwin10-gcc-4.2.1: no input files

If you get ``gcc: command not found`` then you need to install the
developer tools. **If you already have the developer tools installed, you can
proceed to the next section**.

There are several ways to install XCode:

* The developer tools should be present on one of the installation DVDs
  that came with your Mac. Often, this can be found on DVD 2 rather than on
  the main DVD.

* If you don't have the original installation DVDs, you can `register
  <http://developer.apple.com/programs/register/>`_ for free as an Apple
  Developer, which will give you access to XCode 2 or 3:

  - If you are using MacOS 10.6 you should be able to download XCode 3.2.6
    once you are logged in to the `Mac Dev Center
    <http://developer.apple.com/devcenter/mac/index.action>`_. Then, run
    the installer (``Xcode and iOS SDK``).

  - If you are using MacOS 10.5, first log in to the `Mac Dev Center
    <http://developer.apple.com/devcenter/mac/index.action>`_, then go
    `here
    <http://connect.apple.com/cgi-bin/WebObjects/MemberSite.woa/wa/downloads>`_.
    Click on `Developer Tools`, and download `Xcode 3.1.4 Developer DVD
    (Disk Image)`, then run the installer (``XcodeTools.mpkg``).

  - If you are using MacOS 10.4, first log in to the `Mac Dev Center
    <http://developer.apple.com/devcenter/mac/index.action>`_, then go
    `here
    <http://connect.apple.com/cgi-bin/WebObjects/MemberSite.woa/wa/downloads>`_.
    Click on `Developer Tools`, and download `Xcode 2.5 Developer Tools
    (Disk Image)`, then run the installer (``XcodeTools.mpkg``).

* If you like to live on the bleeding edge, have MacOS X 10.6.6, and don't
  mind shelling out $4.99, go to the App Store (``/Applications/App
  Store.app``) and buy XCode 4. Note that while this should work, we have
  not tested it so we can't guarantee that everything will go smoothly with
  the Enthought Python Distribution.

Fortran (Optional)
~~~~~~~~~~~~~~~~~~

You may at some point come across packages which require a Fortran
compiler, or you may want to interface Fortran and Python code. If not, you
can proceed to the next section.

The preferred compiler to interface Fortran and Python code is ``gfortran``.
Other compilers `should` work, but if you want to be on the safe side, you
can download a one-click installer for gfortran 4.2.3 from `this page
<http://r.research.att.com/tools/>`_. Once you have installed it, make sure
that typing ``gfortran`` gives something like this::

    $ gfortran
    i686-apple-darwin8-gfortran-4.2: no input files

If you get ``gfortran: command not found``, then ``gfortran`` did not
install correctly.

