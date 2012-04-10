import matplotlib
matplotlib.use('Agg')
import numpy as np

import matplotlib.pyplot as plt

plt.figure()
plt.subplot(1, 1, 1)
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.savefig('procedural.png', facecolor='0.95')

fig = plt.figure()  # create a figure object
ax = fig.add_subplot(1, 1, 1)  # create an axes object in the figure
ax.plot([1, 2, 3, 4])
ax.set_ylabel('some numbers')
plt.savefig('procedural.png', facecolor='0.95')

fig = plt.figure()  # create a figure object
ax = fig.add_subplot(1, 1, 1)  # create an axes object in the figure
fig.savefig('subplot.png', facecolor='0.95')

fig = plt.figure()
ax = fig.add_axes([0., 0., 1., 1., ])
fig.savefig('axes_full.png', facecolor='0.95')

fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.4, 0.8])
ax2 = fig.add_axes([0.5, 0.1, 0.4, 0.8])
fig.savefig('two_axes.png', facecolor='0.95')

fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.72, 0.72, 0.16, 0.16])
fig.savefig('axes_inset.png', facecolor='0.95')

# Initialize the figure and subplot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Set the font size via a keyword argument
ax.set_title("My plot", fontsize='large')

# Retrieve an element of a plot and set properties
for tick in ax.xaxis.get_ticklabels():
    tick.set_fontsize('large')
    tick.set_fontname('Times New Roman')
    tick.set_color('blue')
    tick.set_weight('bold')
    
fig.savefig('appearance_fonts_custom.png', facecolor='0.95')

plt.rc('xtick', color='r', labelsize='medium', direction='out')
plt.rc('xtick.major', size=4, pad=4)
plt.rc('xtick.minor', size=2, pad=4)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
fig.savefig('appearance_fonts_rc.png', facecolor='0.95')

plt.rcdefaults()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x = np.linspace(1., 8., 30)
ax.plot(x, x ** 1.5, 'ro', label='density')
ax.plot(x, 20/x, 'bx', label='temperature')
ax.legend()
fig.savefig('legend.png', facecolor='0.95')

plt.rc('legend', fontsize='small')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x = np.linspace(1., 8., 30)
ax.plot(x, x ** 1.5, 'ro', label='density')
ax.plot(x, 20/x, 'bx', label='temperature')
ax.legend()
fig.savefig('legend_custom.png', facecolor='0.95')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
image = np.random.poisson(10., (100, 80))
i = ax.imshow(image, interpolation='nearest')
fig.colorbar(i)  # note that colorbar is a method of the figure, not the axes
fig.savefig('colorbar_ax.png', facecolor='0.95')

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.6,0.8])
image = np.random.poisson(10., (100, 80))
i = ax.imshow(image, interpolation='nearest')
colorbar_ax = fig.add_axes([0.7, 0.1, 0.1, 0.8])
fig.colorbar(i, cax=colorbar_ax)
fig.savefig('colorbar_cax.png', facecolor='0.95')

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.6,0.8])
image = np.random.poisson(10., (100, 80))
i = ax.imshow(image, aspect='auto', interpolation='nearest')
colorbar_ax = fig.add_axes([0.7, 0.1, 0.1, 0.8])
fig.colorbar(i, cax=colorbar_ax)
fig.savefig('colorbar_cax_aspect.png', facecolor='0.95')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xticks([0.1, 0.5, 0.7])
ax.set_yticks([0.2, 0.4, 0.8])
fig.savefig('custom_ticks_1.png', facecolor='0.95')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xticks([0.1, 0.5, 0.7])
ax.set_xticklabels(['a', 'b', 'c'])
ax.set_yticks([0.2, 0.4, 0.8])
ax.set_yticklabels(['first', 'second', 'third'])
fig.savefig('custom_ticks_2.png', facecolor='0.95')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xticks([])
fig.savefig('custom_ticks_3.png', facecolor='0.95')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xticklabels('')
fig.savefig('custom_ticks_4.png', facecolor='0.95')

fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(1,1,1)
plt.plot([1, 2, 3, 4])
ax.set_xlabel('The x values')
ax.set_ylabel('The y values')
fig.savefig('publication_1.png', dpi=72/2)

fig = plt.figure(figsize=(1,0.75))
ax = fig.add_subplot(1,1,1)
plt.plot([1, 2, 3, 4])
ax.set_xlabel('The x values')
ax.set_ylabel('The y values')
fig.savefig('publication_2.png', bbox_inches='tight', dpi=72*4)

fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(1,1,1)
plt.plot([1, 2, 3, 4])
ax.set_xlabel('The x values')
ax.set_ylabel('The y values')
fig.savefig('publication_3.png', bbox_inches='tight')

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1,1,1)
plt.plot([1, 2, 3, 4])
ax.set_xlabel('The x values')
ax.set_ylabel('The y values')
fig.savefig('publication_4.png', bbox_inches='tight')

plt.rc('font', family='serif')

fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(1,1,1)
plt.plot([1, 2, 3, 4])
ax.set_xlabel('The x values')
ax.set_ylabel('The y values')
fig.savefig('publication_serif.png', bbox_inches='tight')

plt.rc('font', family='serif')
plt.rc('xtick', labelsize='x-small')
plt.rc('ytick', labelsize='x-small')

fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(1,1,1)
plt.plot([1, 2, 3, 4])
ax.set_xlabel('The x values')
ax.set_ylabel('The y values')
fig.savefig('publication_fontsize.png', bbox_inches='tight')

plt.rc('font', family='serif')
plt.rc('xtick', labelsize='x-small')
plt.rc('ytick', labelsize='x-small')

fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(1,1,1)
x = np.linspace(1., 8., 30)
ax.plot(x, x ** 1.5, color='k', ls='solid')
ax.plot(x, 20/x, color='0.50', ls='dashed')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Temperature (K)')
fig.savefig('publication_lines.png', bbox_inches='tight')
