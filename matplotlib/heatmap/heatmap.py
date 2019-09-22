#!/usr/bin/env python


import matplotlib.pyplot as plt
import numpy as np


w = 20
h = 20
d = 80
plt.figure(figsize=(w, h), dpi=d)

#a = np.random.random((16, 16))
a = np.ones((10, 10))
b = np.zeros((10, 10))

X = np.hstack((a,b))
plt.imshow(X, cmap='Blues_r', interpolation='nearest') #cmap options = viridis,Blues_r,hot
plt.colorbar()
plt.show()
