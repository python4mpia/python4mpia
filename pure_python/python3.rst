A Quick Note about Python 3
===========================

There is currently a shift in the Python community as people move from Python 2.x to Python 3.x. The newer version of Python brings a number of improvements to the language, but also breaks backward compatibility. That is to say, programs written in Python 2.x will not necessarily run in Python 3.x. As a result of this, the Python community has been slow to move to the new version, as this requires that all of the pre-existing libraries and modules are updated. Nevertheless, this transition is now almost complete, with many of the large number of add-in packages now compatible with Python 3.x.


Since this transition is not totally complete, we will concentrate on Python 2.x in these workshops. You should be aware that this transition is taking place, and that there will be some changes if you move to Python 3.x. We introduce two of the many differences in the following subsections.

Integer division
----------------

In Python 2.x dividing two integers leads to unexpected results::

    >>> 3 / 2
    1

In Python 3.x this behavior has been fixed::

    >>> 3 / 2
    1.5

The ``print`` statement
----------------------

In Python 3.x, the ``print`` statement has been replaced with the ``print()`` function. The new syntax is therefore::

    >>> print("Hello World!")
    Hello World!

instead of::

    >>> print "Hello World!"
    Hello World!

String formatting
-----------------

Python 2 uses the following syntax for string formatting::

    format_string % values

for example::

    "%s %d" % ('spam', 1)

while Python 3 uses::

    format_string.format(values)

and uses a ``{}`` notation instead of ``%``, for example::

    "{:s} {:d}".format('spam', 1)

Writing future-proof scripts
----------------------------

Python 2.6 and 2.7 already support the new formatting notation, so if you want
to write future-proof scripts, you can already switch to using the new
formatting in Python 2.

In addition, you can also start using the new division and print statement. To do this, simply do::

    from __future__ import division, print_function

e.g. at the start of a script, and you can then use Python 3 syntax for division and printing.
