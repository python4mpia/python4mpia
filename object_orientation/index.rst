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


In Procedural code, there are often large numbers of raw data variables visible to the main program.

Object Oriented Example::

   class mixableString( object ):
       def __init__(self, text):
           self.__text = list(text)

       def mixItUp(self):
           temp = self.__text[3]
           self.__text[3] = self.__text[5]
           self.__text[5] = temp
           temp = self.__text[10]
           self.__text[10] = self.__text[6]
           self.__text[6] = temp

       def get_text(self):
           return "".join(self.__text)

   test_string = mixableString('this is a test')
   test_string.mixItUp()
   print test_string.get_text()


In Object Oriented code, most variables at the main program level are Objects.  Data are stored
within these objects, and are rarely accessible from the main program.

In the above example, the *class mixableString( object ):* defines the format of the object.  Think of it
as a blueprint.  The *__init__(self)* fuction contains a description of the object.  Other
functions describe functions the object can perform or can access the information inside the object::
However, just as a blueprint is not a building, the definition of an object is not very useful until you "instantiate"
the object.  The line *test_string = mixableString('this is a test')* creates a new instance of the mixableString
object.  The line *test_string.mixItUp()* calls the *mixItUp* function in that object, which performs the scrambling.
The line *print test_string.get_text()* prints out the return value of the *get_text* function.

Extending this example a little further::

   test_A = mixableString('this is a test')
   test_B = mixableString('this is another test!')
   test_A.mixItUp()
   print test_A.get_text()
   print test_B.get_text()

This code will produce the following::

   thii st a sest
   this is another test

test_A and test_B are "instances" of the class mixableString.  Actions performed on one instance of a class will only affect
that instance.  Other instances of the same class are left unaffected.

You might have noticed that the member functions always have the variable *self* as the first argument, even when the calling function
passes no arguments (i.e. *test_string.get_text()*).  The *self* variable is so named because it is a self-referential variable.  Each
instance of an object has to be able to separate itself from other instances.  The *self* variable allows python to access the private
data of each individual object instance.

You also might have noticed that private data is stored in variables with the convention *self.__VarName*.  The *self.__* is the Python convention, and
allows each individual object access to its private data.

What are Python Objects?
------------------------
Python Objects are similar to IDL structures, but with important extra features.  Just as in IDL,
you can arbitrarily design the data structure within the object (structure).  The object can contain
whatever data you would like to put into them.  In addition, you can also add functions to the objects,
which allow you to perform operations on the data without "getting your hands dirty" in the main
program.  (Just FYI, you can also create Objects in IDL, but Objects are integral to Python)

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

In this example, fig, ax, and graph are all handles which refer to objects returned by the function calls.  
As previously demonstrated in the *Making Publication Quality Plots* class, you can use these handles to access and modify 
information in the plot.

There is a difference between using objects and an Object-Oriented approach.  It's very difficult
to *NOT* use objects of some sort in a python script.  However, the fact that you're using objects
doesn't mean that you're writing Object-Oriented code.  A full Object-Oriented approach is quite a different
approach to writing code, and is beyond the scope of this workshop.  Without radically changing your approach,
you can still reap the benefits of Objects and considerably clean up your code.


When to use your own Classes and Objects
----------------------------------------
Object oriented programming works well when you have a set of objects (stars, galaxies, etc...) which
all have values or measurements associated with them.  In a procedural program, you might think of
constructing several arrays (i.e. an array for RA, an array for declination, an array for object name,
an array for Stellar Mass, an array for...)  While this is ok and easy for small numbers of variables,
it can quickly become very confusing and spaghettify your code.

When NOT to use your own Classes and Objects
--------------------------------------------
Small programming tasks with few and disparate variables.  Writing your own Objects front-loads the design
of a program.  You can spend hours writing an object, and relatively small amounts of time writing
the code which interacts with the objects, but if you're only using it to do simple tasks,
you'll end up wasting time, both clock time and processor time.
Object Orientation would not be the first choice for sleek numerical calculations.


How to Make Your Own Objects
----------------------------

Making your own objects is fun and easy!  To create your own object, all you need to do is follow the following format::

   class myObject( Object ):
       def __init__(self, init_var):
           self.__var = init_var

       def myFunction_add(self, input_var):
           self.__var += input_var

       def myFunction_getVar(self):
           return self.__var


That's it!  You define the object with the *class* keyword.  The *__init__()* function is the function used to create a 
new instance of an object.  The *__init__()* function is the only required function.  Any other function

Here is a more practical example:  Say you are studying a sample of young stars.  Each star will have several attributes

.. code-block:: python

   class Star( Object ):
       def __init__(self, Name, RA, Dec, Jmag, Hmag, Kmag, SpT):
           self.__Name = Name           #Name of the star
           self.__RA = RA               #Right Ascension (degrees)
           self.__Dec = Dec             #Declination (degrees)
           self.__Jmag = Jmag           #J-band Magnitude
           self.__Hmag = Hmag           #H-band Magnitude
           self.__Kmag = Kmag           #K-band Magnitude
           self.__SpT = SpT             #Spectral Type
           self.__Av = 0.0              #Visual Extinction

       def get_Name(self):
           return self.__Name

       def get_RA(self, segFlag=False):
           if segFlag:
               hours = int(self.__RA/15)
               minutes = int((self.__RA-hours*15)*60/15)
               seconds = (self.__RA-hours*15.0-minutes/60.0*15.0)*3600/15
               return (hours, minutes, seconds)
           else:
               return self.__RA

       def set_Name(self, Name):
           self.__Name = Name

       def calc_Reddening(self):
           self.__Av = photmetricReddening(self.__Jmag, self.__Hmag, self.__Kmag, self.__SpT)

The *Star* class defines an object which has private members __Name, __RA, __Dec, __Jmag, __Hmag, __Kmag, __SpT, and __Av.

Here is an example of how an object like this might be used

.. code-block:: python

   star_list = []

   starA = Star('TWHya', 165.46625, -34.7047, 8.2, 7.6, 7.3, 'K7V')
   star_list.append(starA)
   star_list.append(Star('AlphaBoo', 213.91529, 19.1824, -2.25, -2.81, -2.91, 'K1III'))
   star_list.append(Star('TTauri', 65.495, 19.535, 7.24, 6.24, 5.32, 'G5V'))

Now, we can access either the sexegesimal or decimal Right Ascension::

   star_list[0].get_RA(segFlag=True)
   >> (11, 1, 51.900000000000546)
   star_list[1].get_RA()
   >> 213.91529


Other Cool Stuff
----------------

If you type *print star_list*, you'll get something akin to this::

   print star_list
   >> [<__main__.Star at 0x104f4d0>,
       <__main__.Star at 0x104f450>,
       <__main__.Star at 0x104f490>]

Not exactly legible, but by overloading the *__repr__(self)*, you can overload the text-representation of a Star object::

   class Star( object ):
      ...
      def __repr__(self):
          return '%s: %f' % (self.__name, self.__RA)

Now, when you ask Python to print a Star object, it calls this function.  So, repeating the previous exercise::

   print star_list
   >> [TWHya: 165.466250, AlphaBoo: 213.915290, TTauri: 65.495000]

You can also overload the "less-than" or "greater-than" operations.  This is powerful because Python
now knows how to compare objects of this type, and can sort them.  So, in the example above, we could
redefine the less-than/greater-than operations to sort a list of stars by Right Ascension (or J-band magnitude,
or alphabetically by name, or whatever you like).  To do this, you must include in the *class* defintion
your new defintion of less-than/greater-than::

   class Star( object ):
      ...
      def __lt__(self, other):
          if isinstance(other, float):
              return self.__RA < other
          else:
              return self.__RA < other.__RA


Now, we can sort the any list of Star objects by Right Ascension::

   star_list.sort()
   print star_list
   >> [TTauri: 65.495000, TWHya: 165.466250, AlphaBoo: 213.915290]

Custom Objects are extremely powerful ways to organize your data and keeping your code from turning into spaghetti.
These are just a few of the things which are possible.  The sky's the limit, so feel free to explore!

+---+
|   |
+---+

.. :Authors:
.. :Copyright:
