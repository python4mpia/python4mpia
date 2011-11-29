
# Can all the needed modules be found?
import numpy as np
import matplotlib.pyplot as plt
import scipy

# labels set in plot command will show up in legend
plt.plot([1,10],[1,10],label='my first line')
# put Greek letters, superscripts + subscripts in labels just like in a TeX file
plt.xlabel(r'log$_{10}$ ($\rho$)')
plt.ylabel('n [cm$^{-3}$]')
plt.title('My First Plot')
# loc=0 automatically chooses the best place to put the legend
plt.legend(loc=0)
