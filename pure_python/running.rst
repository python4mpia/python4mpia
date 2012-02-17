Running Python code
===================

Before we learn about the actual Python language, we need to know where to
enter it. Python can be used either interactively, or from scripts. There is
not one right way to do it, and it depends whether you are interested in an
interactive exploratory analysis, or running or re-running a more complex
program.

Interactive use
---------------

To run Python code interactively, one can use the standard Python prompt, which can be launched by typing ``python`` in your standard shell::

    $ python
    Python 2.7.2 (default, Nov  5 2011, 20:09:20)
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

The ``>>>`` indicates that Python is ready to accept commands. If you type ``a=1`` then press enter, this will assign the value ``1`` to ``a``. If you then type ``a`` you will see the value of ``a`` (this is equivalent to ``print a``)::

    >>> a = 1
    >>> a
    1

The Python shell can execute any Python code, even multi-line statements, though it is often more convenient to use Python non-interactively for such cases.

The default Python shell is limited, and in practice, you will want instead to use the IPython (or interactive Python) shell. This is an add-on package that adds many features to the default Python shell, including the ability to edit and navigate the history of previous commands, as well as the ability to tab-complete variable and function names. To start up IPython, type::

    $ ipython
    Python 2.7.2 (default, Nov  5 2011, 20:09:20)
    Type "copyright", "credits" or "license" for more information.

    IPython 0.11 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]:

The ``>>>`` symbols are now replaced by ``In [x]``, and output, when present, is prepended with ``Out [x]``. If we now type the same commands as before, we get::

    In [1]: a = 1

    In [2]: a
    Out[2]: 1

If you now type the up arrow twice, you will get back to ``a = 1``.

.. note:: IPython is much more than just a Python shell with a few
          improvements compared to the default shell. See the `IPython
          documentation <http://ipython.org/>`_ for a full overview of its
          capabilities!

Running scripts
---------------

While the interactive Python mode is very useful to exploring and trying out code, you will eventually want to write a script to record and reproduce what you did, or to do things that are too complex to type in interactively (defining functions, classes, etc.). To write a Python script, just use your favorite code editor to put the code in a file with a ``.py`` extension. For example, we can create a file called ``test.py`` containing::

    a = 1
    print a

We can then run the script on the command-line with::

    $ python test.py
    1

.. note:: The ``print`` statement is necessary, because typing ``a`` on its own will only print out the value in interactive mode. In scripts, the printing has to be explicitly requested with the print command. To print multiple variables, just separate them with a comma after the print command: ``print a, 1.5, "spam"``. To print variable within strings use the following syntax: ``print ("This is a integer: %d, this is a float: %f, and is a string: %s" % (5, 3.141, "spam"))``

Executable Scripts
------------------

It is also possible to make Python scripts executable. Simply add ``#!/usr/bin/env python`` on the first line of your ``test.py`` script and change the file permission to make it executable with ``chmod +x test.py``. Now the script can be run without the preceeding ``python`` command; instead you can just type ``./test.py`` in the command line. Note that this will only work on Linux and Macs, not on Windows.

Combining interactive and non-interactive use
---------------------------------------------

It can sometimes be useful to run a script to set things up, and to continue in interactive mode. This can be done using the ``%run`` IPython command to run the script, which then gets executed. The IPython session then has access to the last state of the variables from the script::

    $ ipython
    Python 2.7.2 (default, Nov  5 2011, 20:09:20)
    Type "copyright", "credits" or "license" for more information.

    IPython 0.11 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: %run test.py
    1

    In [2]: a + 1
    Out[2]: 2



