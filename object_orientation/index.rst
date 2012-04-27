.. _guide:

Object Oriented Programming in Python
=====================================

What is Object Oriented (00) Programming?
-----------------------------------------
Object Oriented Programming is a philosophy of programming which compartmentalizes data and related
functions into "Objects"

Non-Object Oriented Programming (Procedural Programming) can be thought of as a long, ordered list
of instructions or commands.  Data is visible to the top-level program, and shepharded through the
commands from beginning to end.

Procedural Example::


   def mixItUp(original):
       characters = list(original)
       temp = characters[3]
       characters[3] = characters[5]
       characters[5] = temp
       temp = characters[10]
       characters[10] = characters[6]
       characters[6] = temp
       return "".join(characters)

   test_string = 'this is a test'
   output_string = mixItUp(test_string)
   print test_string
   print output_string


Object Oriented Example::

   class mixableString( object ):
       def __init__(self, text):
           self.text = list(text)

       def mixItUp(self):
           temp = self.text[2]
           self.text[2] = self.text[5]
           self.text[5] = temp
           temp = self.text[10]
           self.text[10] = self.text[6]
           self.text[6] = temp

       def get_text(self):
           return "".join(self.text)

   test_string = mixableString('this is a test')
   test_string.mixItUp()
   print test_string.get_text()


In Procedural code, there are often large numbers of raw data variables visible to the main program.
In Object Oriented code, most variables at the main program level are Objects.  Data are stored
within these objects, and are rarely accessible from the main program

Object Oriented code 

You've Already Been Using OO!
-----------------------------
Any python data variable or function to which you can apply tab completion is an object.

Lists behave like objects::

   E = []
   for n in range(5):
       E.append(n)

append() is a function associated with the list, and its function is to add the value 'n' to the end
of the list 'E'.  If you type "E." and press tab, you see that lists are objects and have the following
member functions associated with them::

   E.append()
   E.extend()
   E.insert()
   E.remove()
   E.sort()
   E.count()
   E.index()
   E.pop()
   E.reverse()

Here is an example from scipy::

   import numpy as np
   from scipy import interpolate
   x = np.arange(0, 10)
   y = np.exp(-x/3.0)
   f = interpolate.interp1d(x, y)
   xnew = np.arange(0,9, 0.1)
   ynew = f(xnew)   # use interpolation function returned by `interp1d`

f is a python function/object returned by the interpolate.interp1d.  When you call the function/object
with a new set of x values, it will perform the interpolation and return interpolated y values.

One of the most obvious objects commonly used in Python is the matplotlib.pyplot object::

   import matplotlib.pyplot as plt
   fig = plt.figure(0)
   ax = fig.add_subplot(1,1,1)
   graph = ax.plot([1,2,3], [6,5,4])

In this example, fig, ax, and graph are all objects derived from the pyplot object

What are Python Objects?
------------------------
Python Objects are similar to IDL structures, but with important extra features.  Just as in IDL,
you can arbitrarily design the data structure within the object (structure).  The object can contain
whatever data you would like to put into them.  In addition, you can also add functions to the objects,
which allow you to perform operations on the data without "getting your hands dirty" in the main
program.

When to use an Object Oriented approach
---------------------------------------
Object oriented programming works well when you have a set of objects (stars, galaxies, etc...) which
all have values or measurements associated with them.  In a procedural program, you might think of
constructing several arrays (i.e. an array for RA, an array for declination, an array for object name,
an array for Stellar Mass, an array for...)  While this is ok and easy for small numbers of variables,
it can quickly become very confusing and spaghettify your code.

When NOT to use an Object Oriented approach
-------------------------------------------
Small programming tasks with few and disparate variables.  Object Orientation front-loads the design
of a program.  You can spend hours writing an object, and relatively small amounts of time writing
the code which interacts with the objects, but if you're only using it to do simple tasks,
you'll end up wasting time.  Object Orientation would not be the first choice for 


How to Make Your Own Objects
----------------------------

Here is a more practical example:  If you are studying a star cluster, it might be useful
to make an Object which contains all the information you care about for a single star.  Here is an 
example of how to define an object::

   class Star(object):
       def __init__(self, name, RA, dec, Jmag, Hmag, Kmag, SpT):
           self.name = name
           self.RA = RA
           self.dec = dec
           self.Jmag = Jmag
           self.Hmag = Hmag
           self.Kmag = Kmag
           self.SpT = SpT

       def getName(self):
           return self.name

       def setName(self):
           return self.name

       def computeReddening(self):
           self.Av = calcReddening(self.Jmag, self.Hmag, self.SpT)
           return self.Av

Each Star object will now have a place for name, RA, dec, Jmag, Hmag, Kmag, and Spectral type.

Each class *must* have a __init__ function, which tells Python how to go about creating a new
instance of the object.  Other than that, the contents of the objects are totally up to you.


Other Cool Stuff
----------------

You can overload the "less-than" or "greater-than" operations.  This is powerful because Python
now knows how to compare objects of this type, and can sort them.  So, in the example above, we coud
redefine the 

+---+
|   |
+---+

.. :Authors:
.. :Copyright:
