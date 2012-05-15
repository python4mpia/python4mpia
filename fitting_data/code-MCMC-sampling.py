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

# Define logarithmic likelihood function.
# params ... array of fit params, here just alpha
# D      ... sum over log(M_n)
# N      ... number of data points.
# M_min  ... lower limit of mass interval
# M_max  ... upper limit of mass interval
def evaluateLogLikelihood(params, D, N, M_min, M_max):
      alpha = params[0]  # extract alpha
      # Compute normalisation constant.
      c = (1.0 - alpha)/(math.pow(M_max, 1.0-alpha) 
                          - math.pow(M_min, 1.0-alpha))
      # return log likelihood.
      return N*math.log(c) - alpha*D
  
# Generate toy data.
N      = 1000000  # Draw 1 Million stellar masses.
alpha  = 2.35
M_min  = 1.0
M_max  = 100.0
Masses = sampleFromSalpeter(N, alpha, M_min, M_max)
LogM   = numpy.log(numpy.array(Masses))
D      = numpy.mean(LogM)*N

# initial guess for alpha.
guess = [3.0]
# Prepare storing MCMC chain.
A = [guess]
# define stepsize of MCMC.
stepsizes = [0.005]
accepted  = 0.0

# Metropolis-Hastings with 10,000 iterations.
for n in range(10000):
      old_alpha  = A[len(A)-1]  # old parameter value.
      old_loglik = evaluateLogLikelihood(old_alpha, D, N, M_min, 
                      M_max)
      # Suggest new candidate from Gaussian proposal distribution.
      new_alpha = numpy.zeros([len(old_alpha)])
      for i in range(len(old_alpha)):
          new_alpha[i] = random.gauss(old_alpha[i], stepsizes[i])
      new_loglik = evaluateLogLikelihood(new_alpha, D, N, M_min, 
                      M_max)
      # Accept new candidate in Monte-Carlo fashing.
      if (new_loglik > old_loglik):
          A.append(new_alpha)
          accepted = accepted + 1.0  # monitor acceptance
      else:
          u = random.uniform(0.0,1.0)
          if (u < math.exp(new_loglik - old_loglik)):
              A.append(new_alpha)
              accepted = accepted + 1.0  # monitor acceptance
          else:
              A.append(old_alpha)

print "Acceptance rate = "+str(accepted/10000.0)


# Discard first half of MCMC chain and thin out the rest.
Clean = []
for n in range(5000,10000):
      if (n % 10 == 0):
          Clean.append(A[n][0])

print "Mean:  "+str(numpy.mean(Clean))
print "Sigma: "+str(numpy.std(Clean))

plt.figure(1)
plt.hist(Clean, 20, histtype='step', lw=3)
plt.xticks([2.346,2.348,2.35,2.352,2.354],
             [2.346,2.348,2.35,2.352,2.354])
plt.xlim(2.345,2.355)
plt.xlabel(r'$\alpha$', fontsize=24)
plt.ylabel(r'$\cal L($Data$;\alpha)$', fontsize=24)
plt.savefig('example-MCMC-results.png')
#plt.show()



# Define gradient of log-likelihood.
def evaluateGradient(params, D, N, M_min, M_max, log_M_min, log_M_max):
    alpha = params[0]  # extract alpha
    grad = log_M_min*math.pow(M_min, 1.0-alpha) - log_M_max*math.pow(M_max, 1.0-alpha)
    grad = 1.0 + grad*(1.0 - alpha)/(math.pow(M_max, 1.0-alpha) - math.pow(M_min, 1.0-alpha))
    grad = -D - N*grad/(1.0 - alpha)
    return numpy.array(grad)

log_M_min  = math.log(1.0)
log_M_max  = math.log(100.0)
# Initial guess for alpha as array.
guess = [3.0]
# Prepare storing MCMC chain.
A = [guess]
# define stepsize of MCMC.
stepsize = 0.000047
accepted = 0.0

import copy
  
# Hamiltonian Monte-Carlo.
for n in range(10000):
      old_alpha  = A[len(A)-1]
      # Remember, energy = -loglik
      old_energy = -evaluateLogLikelihood(old_alpha, D, N, M_min, 
                        M_max)
      old_grad   = -evaluateGradient(old_alpha, D, N, M_min,  
                        M_max, log_M_min, log_M_max)
      
      new_alpha = copy.copy(old_alpha)  # deep copy of array
      new_grad  = copy.copy(old_grad)   # deep copy of array
      # Suggest new candidate using gradient + Hamiltonian dynamics.
      # draw random momentum vector from unit Gaussian.
      p = random.gauss(0.0, 1.0)
      H = numpy.dot(p,p)/2.0 + old_energy    # compute Hamiltonian
      
      # Do 5 Leapfrog steps.
      for tau in range(5):
          # make half step in p
          p         = p - stepsize*new_grad/2.0
          # make full step in alpha
          new_alpha = new_alpha + stepsize*p
          # compute new gradient
          new_grad  = -evaluateGradient(old_alpha, D, N, M_min,  
                           M_max, log_M_min, log_M_max)
          # make half step in p
          p         = p - stepsize*new_grad/2.0
      
      # Compute new Hamiltonian. Remember, energy = -loglik.
      new_energy = -evaluateLogLikelihood(new_alpha, D, N, M_min,
                       M_max)
      newH       = numpy.dot(p,p)/2.0 + new_energy
      dH         = newH - H
      
      # Accept new candidate in Monte-Carlo fashion.
      if (dH < 0.0):
          A.append(new_alpha)
          accepted = accepted + 1.0
      else:
          u = random.uniform(0.0,1.0)
          if (u < math.exp(-dH)):
              A.append(new_alpha)
              accepted = accepted + 1.0
          else:
              A.append(old_alpha)

print "Acceptance rate = "+str(accepted/float(len(A)))

# Discard first half of MCMC chain and thin out the rest.
Clean = []
for n in range(len(A)/2,len(A)):
    if (n % 10 == 0):
        Clean.append(A[n][0])

print "Mean:  "+str(numpy.mean(Clean))
print "Sigma: "+str(numpy.std(Clean))

plt.figure(2)
plt.hist(Clean, 20, histtype='step', lw=3)
plt.xticks([2.346,2.348,2.35,2.352,2.354],
           [2.346,2.348,2.35,2.352,2.354])
plt.xlim(2.345,2.355)
plt.xlabel(r'$\alpha$', fontsize=24)
plt.ylabel(r'$\cal L($Data$;\alpha)$', fontsize=24)
plt.savefig('example-HamiltonianMC-results.png')
plt.show()
