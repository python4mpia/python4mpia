Importing Modules
=================

One of the strengths of Python is that there are many built-in add-ons - or
*modules* - which allow you to do complex tasks in only a few lines of code. In addition, there are many other third-party modules (e.g. Numpy, Scipy,
Matplotlib) that can be installed, and you can also develop your own modules
that include functionalities you commonly use.

The built-in modules are referred to as the *Standard Library*, and you can
find a full list of the available functionality in the `Python Documentation
<http://docs.python.org/library/index.html>`_.

To use modules in your Python session or script, you need to import them. The
following example shows how to import the built-in ``os`` module, which
contains amongst other things many useful functions relating to files and
paths:

    >>> import os

This will give you access to functions available within this module, which you
can now access if you use the module name as a prefix. For example, if we want
to check if a file ``data/m31.fits`` exists, we can use the ``os.path.exists``
function:

    >>> os.path.exists('data/m31.fits')
    False

In this case, we can use the function in an ``if`` statement, since it returns a boolean::

    >>> if os.path.exists('data/m31.fits'):
    ...     print "The file exists"
    ... else:
    ...     print "The file does not exist"
    ...
    The file does not exist

.. note:: As with objects in Python, once you have imported a module, you can
          (in IPython) type the name of the module, followed by ``.``, then
          press TAB to see the available functions!

If a module name is too long to be conveniently written each time you want to use a function, you can define a shortcut when you import it::

    >>> import matplotlib.pyplot as plt
    >>> fig = plt.figure()

In the following workshops we will look a number of third-party modules in
more detail, such as ``numpy`` for creating and manipulating high performance
arrays, ``scipy`` for scientific computing and ``matplotlib.pyplot`` for
plotting.