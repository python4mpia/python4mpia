import numpy

# The function whose square is to be minimised.
# params ... list of parameters tuned to minimise function.
# Further arguments:
# xdata ... design matrix for a linear model.
# ydata ... observed data.
def func(params, xdata, ydata):
	return (ydata - numpy.dot(xdata, params))

# Generate artificial data = straight line with a=0 and b=1 plus some noise.
xdata = numpy.transpose(numpy.array([[1.0,1.0,1.0,1.0,1.0,1.0],[0.0,1.0,2.0,3.0,4.0,5.0]]))
ydata = numpy.array([0.1,0.9,2.2,2.8,3.9,5.1])
x0    = numpy.array([0.0, 0.0])



import scipy.optimize as optimization

print optimization.leastsq(func, x0, args=(xdata, ydata))

print optimization.leastsq(func, x0, args=(xdata, ydata), full_output=True, maxfev=1000)


def func(x, a, b, c):
     return a + b*x + c*x*x
     
xdata = numpy.array([0.0,1.0,2.0,3.0,4.0,5.0])
sigma = numpy.array([1.0,1.0,1.0,1.0,1.0,1.0])
x0    = numpy.array([0.0, 0.0, 0.0])

print optimization.curve_fit(func, xdata, ydata, x0, sigma)


