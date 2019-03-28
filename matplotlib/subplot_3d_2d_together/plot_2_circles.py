#!/usr/bin/env python

import pickle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from mpl_toolkits.mplot3d import axes3d




(X, Y, frac0, frac1) = pickle.load( open( "mydataset.p", "rb" ) )
X3d = np.sum(X*X, axis=1)
X3d = np.reshape(X3d,(800,1))
X3d = np.hstack((X,X3d))

plt.subplot(121)
plt.plot(X[:,0], X[:,1], 'b.')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data in original space, $[x,y]$')

plt.subplot(122, projection='3d')
ax = plt.gca(projection='3d')

plt.plot(X3d[:,0], X3d[:,1], X3d[:,2], 'b.')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('Data in feature space, $[x,y,x^2+y^2]$')
plt.tight_layout()

plt.show()

import pdb; pdb.set_trace()

