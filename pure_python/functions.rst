Writing Functions
=================

As with other languages, you can write functions in Python to avoid repeating code and to improve flow of your programs. Functions use a similar indented syntax to the loops introduced earlier, with a colon after the function name and the following lines indented. As with loops, it is considered good python style to indent with four blank space. Let's start by defining a simple functions::

    def my_function():
        print "Hello World!"
        return  
        
This can be called with ``my_function()``. This is a rather boring function that does not take or return any arguments. Let's make things a little more complicated::

    def add_two_numbers(x1, x2):
        total = x1 + x2
        return total

This function simply adds the two numbers that it is given as arguments. As you expect, we can pass integers, floats and strings to a function. Let's consider a function that operates on a string::

    def mpia_director(name="Hans-Walter Rix"):
        print ("The managing director of MPIA is " + name)
        return

In this example, we have defined what the default value of the name variable in the function. If you try and call this function without any arguments, the default will be used. If you call it with an argument, the specified value will be used. 

        

