#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np

class line_plot:
	def __init__(self):
		pass

	def plot_line(self, X, Y, title, xlabel, ylabel, outpath=None):
		self.add_plot(X,Y)
		self.set_title(title)
		self.set_xlabel(xlabel)
		self.set_ylabel(ylabel)

		if outpath is None: plt.show()


	def set_title(self, title, fontsize=17):
		plt.title(title, fontsize=fontsize)

	def set_xlabel(self, xlabel, fontsize=17):
		plt.xlabel(xlabel, fontsize=fontsize)

	def set_ylabel(self, ylabel, fontsize=17):
		plt.ylabel(ylabel, fontsize=fontsize)

	def add_plot(self, X,Y, color='blue'):
		#color='blue'        # specify color by name
		#color='g'           # short color code (rgbcmyk)
		#color='0.75'        # Grayscale between 0 and 1
		#color='#FFDD44'     # Hex code (RRGGBB from 00 to FF)
		#color=(1.0,0.2,0.3) # RGB tuple, values 0 to 1
		#color='chartreuse'; # all HTML color names supported

		plt.plot(X,Y, color=color)

	def show(self):

		plt.show()



if __name__ == "__main__":
	x = np.linspace(0, 10, 1000)
	y = np.sin(x)

	lp = line_plot()
	lp.plot_line(x, y, 'Title Here', 'X axis', 'Y axis')#, outpath)
