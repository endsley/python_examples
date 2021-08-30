#!/usr/bin/env python

d = {}
d['p1'] = 1
d['p2'] = 2
#d['p3'] = 3
def f2(p1,p2,p3=2):
	print(p1, p2, p3)

f2(**d)
