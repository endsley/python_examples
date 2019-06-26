#!/usr/bin/env python

import numpy as np
from sklearn.preprocessing import KernelCenterer
from sklearn.metrics.pairwise import pairwise_kernels
import sklearn.metrics
import matplotlib.pyplot as plt





X1 = np.array([[0,0],[1,0],[3,4],[4,4]])
X2 = np.array([[0,0],[1,0],[7,8],[8,8]])

D1 = sklearn.metrics.pairwise.pairwise_distances(X1)
D2 = sklearn.metrics.pairwise.pairwise_distances(X2)

X1_max_dis = np.max(D1)
X2_max_dis = np.max(D2)
ratio = X2_max_dis/X1_max_dis



H = np.eye(4) - (1.0/4)*np.ones((4,4))
cX1 = H.dot(X1)
cX2 = H.dot(X2)/ratio


plt.subplot(221)
plt.plot(X1[:,0], X1[:,1], 'x')
plt.title('Original')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.subplot(222)
plt.plot(cX1[:,0], cX1[:,1], 'x')
plt.title('Original Centered')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.subplot(223)
plt.plot(X2[:,0], X2[:,1], 'x')
plt.title('Projected')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.subplot(224)
plt.plot(cX2[:,0], cX2[:,1], 'x')
plt.title('Projected scaled centered')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.subplots_adjust(top=0.88, bottom=0.11, left=0.11, right=0.9, hspace=0.295, wspace=0.215)

plt.show()


