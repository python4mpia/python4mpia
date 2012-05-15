Summary
==========================

* Scipy provides least-squares codes (`leastsq` and `curve_fit`) that use a Levenburg-Marquardt gradient method.
* Scipy also provides a Simplex algorithm (`fmin`) for more general problems.
* Not all problems are least-square problems.
* Simplex is robust but inefficient.
* Gradient methods are efficient but not robust (assume convex problem).
* Metropolis-Hastings is robust but efficiency strongly depends on fine-tuning of numerous stepsizes.
* Hamiltonian Monte-Carlo is robust and efficiency depends on fine-tuning of a single stepsize.



What we did not have time to cover:
--------------------

* `making a fancy plot from Monte-Carlo samples <http://python4mpia.github.com/intro/quick-tour.html>`_
* gradient methods (read additional material)
* testing convexity
* `emcee Python package by Foreman-Mackey et al. (2012) <http://arxiv.org/abs/1202.3665>`_
* multistate/nested sampling
* genetic algorithms




Take home messages
---------------------

* There is no ''perfect'' fit algorithm that solves all problems.
* You need to be able to identify and implement the fit algorithm that solves your problem.
* Python is well suited to implement simple and advanced fit algorithms.