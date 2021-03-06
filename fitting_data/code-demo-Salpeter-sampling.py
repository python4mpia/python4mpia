import numpy,math
import matplotlib.pyplot as plt
import random as random

random.seed(1)  # set random seed.

def sampleFromSalpeter(N, alpha, M_min, M_max):
	# Convert limits from M to logM.
	log_M_Min = math.log(M_min)
	log_M_Max = math.log(M_max)
	# Since Salpeter SMF decays, maximum likelihood occurs at M_min
	maxlik = math.pow(M_min, 1.0 - alpha)
	
	# Prepare array for output masses.
	Masses = []
	# Fill in array.
	while (len(Masses) < N):
		# Draw candidate from logM interval.
		logM = random.uniform(log_M_Min,log_M_Max)
		M    = math.exp(logM)
		# Compute likelihood of candidate from Salpeter SMF.
		likelihood = math.pow(M, 1.0 - alpha)
		# Accept randomly.
		u = random.uniform(0.0,maxlik)
		if (u < likelihood):
			Masses.append(M)
	return Masses

def evaluateLogLikelihood(alpha, D, N, M_min, M_max):
	# Compute normalisation constant.
	c = (1.0 - alpha)/(math.pow(M_max, 1.0-alpha) - math.pow(M_min, 1.0-alpha))
	# return log likelihood.
	return N*math.log(c) - alpha*D

# Generate toy data.
N      = 1000000
alpha  = 2.35
M_min  = 1.0
M_max  = 100.0
Masses = sampleFromSalpeter(N, alpha, M_min, M_max)
LogM   = numpy.log(numpy.array(Masses))
D      = numpy.mean(LogM)*N

# initial guess for alpha.
guess = 3.0
# Prepare storing MCMC chain.
A = [guess]
# define stepsize of MCMC.
stepsize = 0.005
accepted = 0.0

# Metropolis-Hastings.
for n in range(10000):
	old_alpha  = A[len(A)-1]
	old_loglik = evaluateLogLikelihood(old_alpha, D, N, M_min, M_max)
	# Suggest new candidate from Gaussian proposal distribution.
	new_alpha  = random.gauss(old_alpha, stepsize)
	new_loglik = evaluateLogLikelihood(new_alpha, D, N, M_min, M_max)
	# Accept new candidate in Monte-Carlo fashing.
	if (new_loglik > old_loglik):
		A.append(new_alpha)
		accepted = accepted + 1.0
	else:
		u = random.uniform(0.0,1.0)
		if (u < math.exp(new_loglik - old_loglik)):
			A.append(new_alpha)
			accepted = accepted + 1.0
		else:
			A.append(old_alpha)

print "Acceptance rate = "+str(accepted/10000.0)

# Discard first half of MCMC chain and thin out the rest.
Clean = []
for n in range(5000,10000):
	if (n % 10 == 0):
		Clean.append(A[n])

plt.figure(1)
plt.hist(Clean, 20, histtype='step', lw=3)
plt.xticks([2.346,2.348,2.35,2.352,2.354],[2.346,2.348,2.35,2.352,2.354])
plt.xlim(2.345,2.355)
plt.xlabel(r'$\alpha$', fontsize=24)
plt.ylabel(r'$\cal L($Data$;\alpha)$', fontsize=24)
plt.savefig('example-MCMC-results.png')
plt.show()
