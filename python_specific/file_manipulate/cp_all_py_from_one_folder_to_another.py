#!/usr/bin/env python

import os
from shutil import copyfile


def copy_code(source, dest):
	for root, subdirs, files in os.walk('./HSIC_For_ML_copy'):
		for fn in files:
			if fn.find(".py") != -1 and fn.find(".pyc") == -1:
				fname = root + '/' + fn
				fname2 = fname.replace(source, dest)
				copyfile(fname, fname2)


if __name__ == "__main__":
	copy_code('HSIC_For_ML_copy', 'HSIC_For_ML')
