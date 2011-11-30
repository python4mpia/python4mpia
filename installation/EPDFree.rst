.. _EPD_Free

EPD Free (Linux, MacOS and Windows)
===================================

These instructions tell you how to install the core scientific Python
packages on either Linux, MacOS, or Windows using the Free Enthought
Python Distribution.

Download EPD
------------

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
to your operating system (Linux, MacOS or Windows).


Linux
-----

Once you have downloaded the appropriate EPD package for your system,
run the installation script. For example::

   bash epd_free-7-1-2-rh5-x86.sh

Next you need to edit the appropriate shell startup file
(e.g. ``~/.cshrc`` or ``~/.bash_profile``) and update your path to
include the EPD path.  For instance if you specified to install EPD in
``/home/me/epd7.1`` then the following will work::

  export PATH=/home/me/epd7.1/bin:$PATH  # bash
  set path=(/home/me/epd7.1/bin $path)   # csh or tcsh

Quick installation check
~~~~~~~~~~~~~~~~~~~~~~~~

Open a new terminal window and type::

  which ipython

You should see::

  /home/me/epd7.1/bin/ipython  

where ``/home/me/epd7.1`` is replaced by your installation root path.


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


MacOS
-----

Assuming that you have downloaded the EPD disk image, open it, then
double-click on ``EPD.mpkg`` and follow the prompts to install. Choose
all the defaults for installing (in particular use the default
installation location).

Quick installation check
~~~~~~~~~~~~~~~~~~~~~~~~

Open a new terminal window and type::

  which ipython

You should see something like:

  /Library/Frameworks/EPD32.framework/Versions/Current/bin/ipython

If EPD installed successfully and you can start ``python`` but not
``ipython`` (error message like ``ipython: command not found``) then
there is likely a problem with your PATH. To fix this, try following
these steps:

Step 1
######

Are you sure you opened a new terminal window after the installation finished?

Step 2
######

Try this in a new terminal window::

  echo $PATH

If you do not see something like
``/Library/Frameworks/EPD32.framework/Versions/Current/bin`` in your path then go
to step 3.  

Step 3
########

Determine if you are running csh/tcsh or bash by entering the command ``ps`` in a terminal window.
For ``csh`` or ``tcsh`` you should edit the file ``~/.cshrc`` and add the following lines at the end::

 # Setting PATH for Enthough Python Distribution
 set path=(/Library/Frameworks/EPD32.framework/Versions/Current/bin $path)

For ``bash`` you should edit the file ``~/.bash_profile`` and add the following lines at the end::

 # Setting PATH for Enthough Python Distribution
 export PATH=/Library/Frameworks/EPD32.framework/Versions/Current/bin:$PATH
