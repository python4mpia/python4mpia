Code Examples
=============

This page contains many examples of applications of Python scripts to Astronomy

Parallel process of FITS images
-------------------------------

::

    import glob
    import multiprocessing

    import pyfits
    from scipy.ndimage import gaussian_filter

    # Define a function to run on files
    def smooth(filename):

        # Read in FITS file
        hdulist = pyfits.open(filename)

        # Convolve the data in the primary HDU
        hdulist[0].data = gaussian_filter(hdulist[0].data, 3)

        # Write out the result to a new file
        hdulist.writeto(filename.replace('.fits', '_smooth.fits'))

    # Search for all FITS files
    files = glob.glob('files/*.fits')

    # Define a 'pool' of 16 processors
    p = multiprocessing.Pool(processes=16)

    # Run the function over all files in parallel
    ap.map(smooth, files)



Making a fancy plot from Monte-Carlo samples
----------------------------------

Assume you have run an MCMC and you are left with two arrays X,Y of MCMC samples of two fit parameters. You now want to use X,Y to visualise the likelihood manifold. You can do that (a) as a simple scatter plot or (b) in a more fancy way::

  import numpy,math
  import pylab

  # Create artificial data mimicking some MCMC results.
  N = 50000
  X = numpy.random.normal(0.0, 1.5, N)  # Normal distribution
  Y = numpy.random.gamma(2.0, 2.0, N)   # Gamma distribution

  # Define plot ranges once, for multiple usage later (e.g. more than a single subplot).
  XRANGE = [-6.4,6.4]
  YRANGE = [-2.4,11.4]

  # Define figure size and formatting
  fig = pylab.figure(1, figsize=(16,7.5))
  fig.subplots_adjust(wspace=0.2, left=0.04, bottom=0.07, top=0.99, right=0.99)

  # Two subplots next to each other. Start with left subplot.
  pylab.subplot(121)
  # Simply plot X vs. Y as data points.
  pylab.plot(X, Y, 'o', ms=4, alpha=0.1, color='blue')

  pylab.xlim(XRANGE)
  pylab.ylim(YRANGE)
  pylab.xticks(fontsize=16)
  pylab.yticks(fontsize=16)
  pylab.xlabel(r'$x$', fontsize=24)
  pylab.ylabel(r'$y$', fontsize=24)

  # Next, make right subplot.
  pylab.subplot(122)

  # Convert to 2d histogram.
  B      = 25
  hist2D = numpy.histogram2d(X, Y, bins=[B,B], range=[XRANGE,YRANGE], normed=False)[0]

  # Plot Monte-Carlo samples as 2D histogram.
  # Beware: imshow switches axes, so switch back.
  hist2D = numpy.transpose(hist2D)
  pylab.imshow(hist2D, cmap=pylab.cm.gray, interpolation='gaussian')

  # Overplot with error contours 1,2,3 sigma.
  maximum    = numpy.max(hist2D)
  # Infering correct levels of 1,2,3 sigma would require some further code,
  # so let's fake it by setting the three levels to some guessed values.
  [L1,L2,L3] = [0.5*maximum,0.25*maximum,0.125*maximum]
  #print [L1,L2,L3]
  cs = pylab.contour(hist2D, levels=[L1,L2,L3], linestyles=['--','--','--'], colors=['orange','orange','orange'], linewidths=1)
  # use dictionary in order to assign my own labels to the contours.
  fmtdict = {L1:r'$1\sigma$',L2:r'$2\sigma$',L3:r'$3\sigma$'}
  pylab.clabel(cs, fmt=fmtdict, inline=True, fontsize=20)

  # Also plot marginal likelihoods.
  S  = 101
  I  = []
  # Bin X,Y separately. As 1D bin, can use more bins now.
  LX = numpy.histogram(X, bins=S, range=XRANGE, normed=True)[0]
  LY = numpy.histogram(Y, bins=S, range=YRANGE, normed=True)[0]
  # Rescale by maxima. Don't want this histogram to span whole subplot.
  rescale_X = 0.15*float(B)/numpy.max(LX)
  rescale_Y = 0.15*float(B)/numpy.max(LY)
  for s in range(S):
	  I.append(float(s)*float(B)/float(S))
	  LX[s] = LX[s]*rescale_X
	  LY[s] = LY[s]*rescale_Y
  pylab.plot(I, LX, '-', lw=3, color='white')
  pylab.plot(LY, I, '-', lw=3, color='white')

  pylab.xlim(0,B-1)
  pylab.ylim(0,B-1)

  # Sadly, through binning numpy looses the position information, so we need to restore it manually
  # in order to plot proper axes ticks.
  T = []
  L = []
  for x in -6,-4,-2,0,2,4,6:
	  index = (x-XRANGE[0])*float(B-1)/(XRANGE[1] - XRANGE[0])
	  T.append(index)
	  L.append(x)
  pylab.xticks(T, L, fontsize=16)

  T = []
  L = []
  for y in -2,0,2,4,6,8,10:
	  index = (y-YRANGE[0])*float(B-1)/(YRANGE[1] - YRANGE[0])
	  T.append(index)
	  L.append(y)
  pylab.yticks(T, L, fontsize=16)

  pylab.xlabel(r'$x$', fontsize=24)
  pylab.ylabel(r'$y$', fontsize=24)

  pylab.savefig('plot_MCMC_samples.png')  # Save figure as png-file.
  pylab.show()

.. image:: plot_MCMC_samples.png