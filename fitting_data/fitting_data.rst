Fitting data with Python
========================

Fitting models to data is one of the key steps in scientific work:

* fitting some spectrum/spectral line
* fitting 2D light distribution of a galaxy
* fitting orbits of exoplanets
* estimating the stellar IMF from a set of observed masses
* estimating the galaxy luminosity function from data
* ...

Numpy and Scipy provide readily usable tools to fit models to data.

Moreover, Python is an excellent environment to develop your own fitting routines for more advanced problems.

Goals of this session
----------------

* This is a Python tutorial but some statistics are inevitable!
* How to use implemented routines: `leastsq`, `curve_fit` and Simplex.
* Astrophysical example: Salpeter mass function.
* Metropolis-Hastings MCMC.
* Hamiltonian Monte-Carlo.

At the end of this session, participants will have code fragments that can be readily used or easily adopted for their own scientific work.


**Agenda**

.. toctree::
   :maxdepth: 1
   
   introduction
   least-squares-fitting
   simplex-fitting
   gradient-methods
   Salpeter-background
   MC-sampling-from-Salpeter
   Metropolis-Hastings
   Hamiltonian-MCMC
   convex-Salpeter-problem
   summary

:Authors: Rene Andrae
:Copyright: 2012, Rene Andrae