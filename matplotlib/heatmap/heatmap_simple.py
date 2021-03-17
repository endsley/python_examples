#!/usr/bin/env python


import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np


def get_Correlation_Matrix(self, path):
	ensure_path_exists(path)

	withY = np.hstack((self.X, np.atleast_2d(self.Y).T))
	df = pd.DataFrame(withY)
	corrMatrix = df.corr()

	m_size = corrMatrix.shape[0]
	yticklabels = np.arange(1, m_size+1)
	xticklabels = np.arange(1, m_size+1)
	ax = sn.heatmap(corrMatrix, annot=True, yticklabels=yticklabels, xticklabels=xticklabels)

	ax.set_title('Linear Correlation Matrix')
	plt.savefig(path + 'Linear_Correlation_Matrix.png')
	plt.clf()



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



