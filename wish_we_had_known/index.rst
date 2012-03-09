.. _wish_we_had_known:


What We Wish We'd Known When We Started Using Python
=============================================================

Debugging 
----------
Use pdb.  It is good ::

   import pdb; pdb.pm()

for tracing back through the stack.  Or else put

   import pdb; pdb.set_trace()

in your code to make your code stop at a point where you to debug.  In the
debugger, the commands you will want to use can be abreviated to 1 character::

   p: print any variable you want at the point you are in the stack trace.
   u: move up the stack
   d: move back down the stack
   l: list the code surrounding the line where you are
   c: continue to let the code run
   n: run just the next line


Catching Errors (try/except)
---------------------------

This is one of the "pythonic" ways of doing things that ends up being 
quick and useful.  If you don't want code to crash someplace where it makes
an error, you can put it in a try statement and tell except to do something
(possibly pass) ::

    try:
        dumb code
    except:
        pass

You can have except catch only certain errors if you want.

Pickle
------

It is very usful to save some of the data that you derive in python for later
use.  Pickle is the way to do this in Python.  For example, if your data
is in some big file that takes a long time to load and you just want the 
profile of some object in it.
It is easy to save a dictionary::

    import pickle
    pickle.dump({'data1':[1,234,6902,3496]},open('outputfile.pkl','w'))

Note that pickle needs to be sent a file object which can be created with
the open method.

Then to load that data back in later

    d = pickle.load(open('outputfile.pkl'))
    d['data1']

Matplotlib Gallery
------------------

When you Google any Matplotlib function, you get directed to this endless
webpage that takes forever to load.  It is generally much better to go
http://matplotlib.sourceforge.net/gallery.html or http://www.scipy.org/Cookbook/Matplotlib

Or else when you're in python use the ``?`` help functionality::

    In[4]: plt.plot?


:Author: Originally written by Tom Aldcroft, with changes by Tom Robitaille and Neil Crighton.
