A Quick Note about Python 3 
===========================

There is currently a shift in the Python community as people move from Python 2.x to Python 3.x. The newer version of Python brings a number of improvements to the language, but also breaks backward compatibility. That is to say, programs written in Python 2.x will not necessarily run in Python 3.x. As a result of this, the Python community has been slow to move to the new version, as this requires that all of the pre-existing libraries and modules are updated. Nevertheless, this transition is now almost complete, with many of the large number of add-in packages now compatible with Python 3.x. 


Since this transition is not totally complete, we will concentrate on Python 2.x in these workshops. You should be aware that this transition is taking place, and that there will be some changes if you move to Python 3.x. We introduce two of the many differences in the following subsections. 

Integer Division
----------------

In Python 2.x dividing two integers leads to unexpected results::

    >>> 3 / 2
    1
    
In Python 3.x this behavior has been fixed::

    >>> 3 / 2
    1.5
    
The ``print`` Statement
----------------------

In Python 3.x, the ``print`` statement has been replaced with the ``print()`` function. The new syntax is therefore::

    >>> print("Hello World!") 
    Hello World!

instead of::
    
    >>> print "Hello World!"
    Hello World!
