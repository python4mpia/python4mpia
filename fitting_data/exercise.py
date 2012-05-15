# Task: Generate data from -5 to +5 with y-values a unit Gaussian + noise with sigma = 0.1.
#       Define the model for curve_fit and call curve_fit.
#       Define chi2 for Simplex and call Simplex.


import numpy,math

# Define model.
def func4curve_fit(x, mu, sigma):
    residual = (x-mu)/sigma
    return numpy.exp(-residual*residual/2.0)

# Create data.
X = []
Y = []
for x in range(-5, 6, 1):
    X.append(x)
    Y.append(math.exp(-x*x/2.0))
# Add Gaussian noise to data.
Y = Y + numpy.random.normal(0.0, 0.1, len(Y))


import scipy.optimize as optimization

guess = [1.0, 2.0]
print optimization.curve_fit(func4curve_fit, X, Y, guess)


def func4Simplex(params, X, Y):
	mu    = params[0]
	sigma = params[1]
	chi2  = 0.0
	for n in range(len(X)):
		residual = Y[n] - func4curve_fit(X[n], mu, sigma)
		chi2 = chi2 + residual*residual
	return chi2

from scipy.optimize import fmin as simplex
print simplex(func4Simplex, guess, args=(X, Y))

