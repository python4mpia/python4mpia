import numpy,math
import matplotlib.pyplot as plt

# Create 1D Gaussian toy data.
numpy.random.seed(1)  # set random seed
# Draw 10 values from unit Gaussian.
Data = numpy.random.normal(0.0, 1.0, 10)

# Our model is a Gaussian with:
# offset a = 0.0
# slope  b = 0.0


# Range of parameter a.
a_min = -2.5
a_max =  2.5
# Range of parameter b.
b_min = -1.0
b_max =  1.0
# Number of steps of grid.
Steps = 51
# Allocate grid as matrix.
Grid  = numpy.zeros([Steps,Steps])
# Try all parameter combinations.
for s1 in range(Steps):
    for s2 in range(Steps):
        # Current parameter combination.
        a = a_min + (a_max - a_min)*float(s1)/float(Steps-1)
        b = b_min + (b_max - b_min)*float(s2)/float(Steps-1)
        
        # Evaluate chi-squared.
        chi2 = 0.0
        for n in range(len(Data)):
            # Use index n as pseudo-position
            residual = (Data[n] - a - n*b)
            chi2     = chi2 + residual*residual
        Grid[Steps-1-s2,s1] = chi2

plt.figure(1, figsize=(8,3))
image = plt.imshow(Grid, vmin=numpy.min(Grid), vmax=numpy.min(Grid)+20.0, extent=[a_min,a_max,b_min,b_max])
plt.colorbar(image)
plt.xlabel(r'$a$', fontsize=24)
plt.ylabel(r'$b$', fontsize=24)
plt.savefig('example-chi2-manifold.png')
plt.show()

