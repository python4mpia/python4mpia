Importing Modules 
=================

One of the strengths of Python is that there are many preexisting add-ons ("'modules'"), which allow you to do complex tasks in only a few lines of code. For example, there are modules for scientific computing, plotting, multiprocessing, graphical user interfaces and databases. The default Python install includes a number of the core modules. In the following workshops we will look a number of these modules in more detail, such as ``numpy`` for scientific computing and ``matplotlib.pyplot`` for plotting. Ultimately, you will start writing your own modules that include functionalities you commonly use.

To include additional modules in your programs, you need to import them::

    >>> import numpy
    
This will give you access to functions available within this module, which you can now access if you use the module name as a prefix. For example, we can now create an array of numbers and perform an operation on them using the ``numpy`` functions ``arange()`` and ``sin()``::

    >>> x = numpy.arange(0, 3.141, 0.01)
    >>> y = numpy.sin(x)
    
If the module name is too long to be conveniently written each time you want to use a function, you can define a shortcut when you import it::

    >>> import matplotlib.pyplot as plt
    
The plotting module ``matplotlib.pyplot`` can now simply be referred to as ``plt``. We can continue the previous example with the ``plot()`` function from this module::

    >>> plt.plot(x,y)
    >>> plt.show()
    
Congratulations, you have just made your first plot. There will be much on ``numpy`` and ``matplotlib.pyplot`` in future workshops.
