#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

from numpy import genfromtxt
from sklearn.preprocessing import KernelCenterer
from sklearn.metrics.pairwise import pairwise_kernels
import sklearn.metrics
import matplotlib.pyplot as plt



pth = 'arth_2'; layers = [1,2,3,4,5,6,7,9]; title = 'Adversarial Dataset : layer output in 1 D'


plt.subplot(111)
for i in layers:
	z = genfromtxt(pth + '/' + str(i) + '/zℓ.csv', delimiter=',')

	y = np.zeros(len(z[0:5])) + i
	if i == 1:
		plt.plot(z[0:5], y, 'x', color='b', label='Class 1')
		plt.plot(z[5:10], y, 'x', color='g', label='Class 2')
	else:
		plt.plot(z[0:5], y, 'x', color='b')
		plt.plot(z[5:10], y, 'x', color='g')

#plt.grid('on')
#plt.yaxis.grid()
#plt.gca().xaxis.grid(True)
plt.gca().yaxis.grid(True, linestyle='dotted')
#plt.grid(linestyle='dotted')
plt.xlabel('Sample Location in IDS', fontsize=17 )
plt.ylabel('Layer ID', fontsize=17)
plt.title(title, fontsize=17)
plt.legend()
plt.tight_layout()
plt.show()
##plt.axhline(y=0, color='k')
##plt.axvline(x=0, color='k')

import pdb; pdb.set_trace()

