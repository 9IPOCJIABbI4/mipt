#!/usr/bin/env python
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['text.usetex'] = True
#plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = [r'\usepackage[utf8]{inputenc}',
            r'\usepackage[english,russian]{babel}',
            r'\usepackage{amsmath}']
x = []
y = []

x1 = np.arange(0,1.22495,0.0001)   # start,stop,step
y1 =0.0016204171195169778 + 0.0021327823398507315 *x1
plt.plot(x1,y1, label=r'$\cos^2 \beta $', color='tab:blue')

#x, y = np.loadtxt('data1.csv', delimiter=';', unpack=True)
#plt.errorbar(x, y, yerr=0.02*y ,fmt='o', label=r'$\mathcal{V}_3 (\beta)$', color='teal')
y,x = np.loadtxt('Untitled.csv', delimiter=',', unpack=True)
plt.errorbar(x, y,fmt='o', label=r'$\mathcal{V}_3 (\beta)$', color='tab:blue')
#x3, y3 = np.loadtxt('data3.csv', delimiter=';', unpack=True)
#plt.errorbar(x3, y3, yerr=0.02*y3 ,fmt='s', label=r'$\mathcal{V}_3 (\beta)$', color='tab:brown')
#y2 = np.cos(x1)
#plt.plot(180*x1/np.pi,y2, label=r'$\cos \beta $', color='orchid')
#plt.legend()
plt.title(r'\begin{center} $1/N(\theta)=A(1-\cos \theta)$\end{center}')
#             r'\frac{-e^{i\pi}}{2^n}$!')
plt.xlabel(r'$1-\cos \theta$')
plt.ylabel(r'$1/N(\theta)$')

plt.grid(True)

# example data
#x = np.arange(0.1, 4, 0.5)
#y = np.exp(-x)

# example variable error bar values
#yerr = 0.1 + 0.2*np.sqrt(x)
#xerr = 0.1 + yerr

# First illustrate basic pyplot interface, using defaults where possible.
#plt.figure()
#plt.errorbar(x, y, xerr=0.2, yerr=0.4,capsize=4, fmt='o')
#plt.title("Simplest errorbars, 0.2 in x, 0.4 in y")

# Now switch to a more OO interface to exercise more features.
#fig, axs = plt.subplots(nrows=2, ncols=2, sharex=True)
#ax = axs[0,0]
#ax.errorbar(x, y, yerr=yerr, fmt='o')
#ax.set_title('Vert. symmetric')

# With 4 subplots, reduce the number of axis ticks to avoid crowding.
#ax.locator_params(nbins=4)

#ax = axs[0,1]
#ax.errorbar(x, y, xerr=xerr, fmt='o')
#ax.set_title('Hor. symmetric')

#ax = axs[1,0]
#ax.errorbar(x, y, yerr=[yerr, 2*yerr], xerr=[xerr, 2*xerr], fmt='--o')
#ax.set_title('H, V asymmetric')
#
#ax = axs[1,1]
#ax.set_yscale('log')
## Here we have to be careful to keep all y values positive:
#ylower = np.maximum(1e-2, y - yerr)
#yerr_lower = y - ylower
#
#ax.errorbar(x, y, yerr=[yerr_lower, 2*yerr], xerr=xerr,
#fmt='o', ecolor='g',capsize=4)
#ax.set_title('Mixed sym., log y')
#
#fig.suptitle('Variable errorbars')
#
plt.show()
plt.savefig("plot.pdf")

