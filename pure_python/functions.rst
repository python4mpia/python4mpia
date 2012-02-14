Writing Functions
=================

As with other languages, you can write functions in Python to avoid repeating code and to improve flow of your programs. Functions use a similar indented syntax to the loops introduced earlier, with a colon after the function name and the following lines indented. As with loops, it is considered good python style to indent with four blank space. Let's start by defining a simple functions::

    def my_function():
        print "Hello World!"
        
This can be called with ``my_function()``. 

.. note:: 
    It is considered good python style to have function names all in lower case, with words separated by underscore to improve readability. 

This is a rather boring function that does not take or return any arguments. Let's make things a little more complicated::

    def add_two_numbers(x1, x2):
        total = x1 + x2
        return total

This function simply adds the two numbers that it is given as arguments. As you expect, we can pass integers, floats and strings to a function. Consider the flowing function::
    
    def print_argument(x = 5):
        print x

In this example, we have defined what the default value of the ``x`` variable in the function. If you try and call this function without any arguments, the default will be used. If you call it with an argument, the specified value will be used.

.. admonition::  Exercise

    Write a function that prints out "The managing director of MPIA is [name]", where [name] is the argument that is given. If no argument is given, [name] should be the default string "Hans-Walter Rix". If the argument "Thomas Henning" is given, the function should print "Thomas Henning was the managing director of MPIA last year".

.. raw:: html

    <p class="flip8">Click to Show/Hide Solution</p> <div class="panel8">

::

    def mpia_director(name="Hans-Walter Rix"):
        if name == "Thomas Henning":
            print ("%s was the managing director of MPIA last year." % name)
        else:
            print ("The managing director of MPIA is " + name + ".")

 

        

