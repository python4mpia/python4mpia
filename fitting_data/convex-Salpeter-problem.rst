Additional material: Convexity of the Salpeter problem
====================

The Salpeter problem is neither a linear nor a least-squares problem. Let us check if it is a convex problem!

For Hamiltonian Monte-Carlo, we have already computed the gradient of the log-likelihood, which is our objective function:

  :math:`\frac{\partial\log\mathcal L}{\partial\alpha} = -D-\frac{N}{1-\alpha}\left[1 + \frac{1-\alpha}{M_{max}^{1-\alpha}-M_{min}^{1-\alpha}}\left(M_{min}^{1-\alpha}\log M_{min}-M_{max}^{1-\alpha}\log M_{max}\right)\right]`

As we only have a single fit parameter - :math:`\alpha` - the Hessian is a 1x1 matrix and its single eigenvalue is:

  :math:`\frac{\partial^2\log\mathcal L}{\partial\alpha^2} = -N\left[\frac{1}{(1-\alpha)^2} + \left(\frac{M_{min}^{1-\alpha}\log M_{min}-M_{max}^{1-\alpha}\log M_{max}}{M_{max}^{1-\alpha}-M_{min}^{1-\alpha}}\right)^2 + \frac{M_{max}^{1-\alpha}\log^2 M_{max}-M_{min}^{1-\alpha}\log^2 M_{min}}{M_{max}^{1-\alpha}-M_{min}^{1-\alpha}}\right]`

If the Salpeter problem is convex, this eigenvalue has to be negative. Is it negative?

By definition, we have :math:`N>0` and :math:`M_{max}>M_{min}`.

Therefore, as long as :math:`\alpha\neq 1`, the first two terms in brackets are always strictly positive.

For :math:`\alpha < 1`, also the third term is strictly positive because :math:`M_{max}>M_{min}`.

For :math:`\alpha > 1`, the third term may in fact become negative. However, for :math:`M_{min}=1` and :math:`M_{max}=100`, the eigenvalue is still strictly negative at least until :math:`\alpha=10`.

We conclude that for :math:`M_{min}=1` and :math:`M_{max}=100` and for all :math:`\alpha < 10` and :math:`\alpha\neq 1` the eigenvalue :math:`\frac{\partial^2\log\mathcal L}{\partial\alpha^2}` of the Hessian is always strictly negative. In other words, in our case the Salpeter problem is convex, i.e., the log-likelihood function has only a single maximum which is therefore the global maximum.

Obviously, we could simply use a gradient method - ideally Newton's method (we already have computed gradient and Hessian!) - in order to find the maximum quickly. Nevertheless, the Monte-Carlo methods also directly provide us with uncertainty estimates.

This is a very rare example, where a non-trivial problem can be directly tested for convexity.