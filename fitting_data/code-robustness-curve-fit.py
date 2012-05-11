import numpy,math
import scipy.optimize as optimization
import matplotlib.pyplot as plt

def func(x, a, b):
	return a + b*b*x

xdata = numpy.array([0.0,1.0,2.0,3.0,4.0,5.0])
ydata = numpy.array([0.1,0.9,2.2,2.8,3.9,5.1])
sigma = numpy.array([1.0,1.0,1.0,1.0,1.0,1.0])

Steps = 101
Chi2Manifold = numpy.zeros([Steps,Steps])
amin = -7.0
amax = +5.0
bmin = -4.0
bmax = +4.0
for s1 in range(Steps):
    for s2 in range(Steps):
	a = amin + (amax - amin)*float(s1)/(Steps-1)
	b = bmin + (bmax - bmin)*float(s2)/(Steps-1)
	
	chi2 = 0.0
	for n in range(len(xdata)):
		residual = (ydata[n] - func(xdata[n], a, b))/sigma[n]
		chi2 = chi2 + residual*residual
	Chi2Manifold[Steps-1-s2,s1] = chi2

plt.figure(1, figsize=(8,4.5))
plt.subplots_adjust(left=0.09, bottom=0.09, top=0.97, right=0.99)
image = plt.imshow(Chi2Manifold, vmax=50.0, extent=[amin, amax, bmin, bmax])

for a_initial in -6.0, -4.0, -2.0, 0.0, 2.0, 4.0:
	# Initial guess.
	x0   = numpy.array([a_initial, -3.5])
	xFit = optimization.curve_fit(func, xdata, ydata, x0, sigma)[0]
	plt.plot([x0[0], xFit[0]], [x0[1], xFit[1]], 'o-', ms=4, markeredgewidth=0, lw=2, color='orange')
plt.colorbar(image)
plt.xlim(amin, amax)
plt.ylim(bmin, bmax)
plt.xlabel(r'$a$', fontsize=24)
plt.ylabel(r'$b$', fontsize=24)
plt.savefig('demo-robustness-curve-fit.png')
plt.show()

