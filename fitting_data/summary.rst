Summary
==========================

* Scipy provides least-squares codes (`leastsq` and `curve_fit`) that use a Levenburg-Marquardt gradient method.
* Scipy also provides a Simplex algorithm (`fmin`) for more general problems.
* Not all problems are least-square problems.
* Simplex is robust but inefficient.
* Gradient methods are efficient but not robust (assume convex problem).
* Fitting a Salpeter SMF is a convex problem.
* Direct Monte-Carlo sampling only works for trivial fit problems (1D, large uncertainties).
* Metropolis-Hastings is robust but efficiency strongly depends on fine-tuning of numerous stepsizes.
* Hamiltonian Monte-Carlo is robust and efficiency depends on fine-tuning of a single stepsize.

Take home messages
---------------------

* There is no ''perfect'' fit algorithm that solves all problems.
* You need to be able to identify and implement the fit algorithm that solves your problem.
* Python is well suited to implement simple and advanced fit algorithms.