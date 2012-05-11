import math
from pylab import *

Mmin = 1.0
Mmax = 100.0
logMmin = math.log(Mmin)
logMmax = math.log(Mmax)

A = []
F = []
for n in range(5001):
	alpha = 1.001 + 9.0*float(n)/5000.0
	
	term_1 = 1.0/(1.0 - alpha)
	
	term_2 = (math.pow(Mmin,1.0-alpha)*logMmin - math.pow(Mmax,1.0-alpha)*logMmax)/(math.pow(Mmax,1.0-alpha) - math.pow(Mmin,1.0-alpha))
	
	term_3 = (math.pow(Mmax,1.0-alpha)*logMmax*logMmax - math.pow(Mmin,1.0-alpha)*logMmin*logMmin)/(math.pow(Mmax,1.0-alpha) - math.pow(Mmin,1.0-alpha))
	
	A.append(alpha)
	F.append(term_1*term_1 + term_2*term_2 + term_3)

figure(1)
plot(A, F, '-', lw=3, color='black')
yscale('log')
show()
