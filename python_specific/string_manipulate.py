#!/usr/bin/env python

import numpy as np

def pretty_np_array(m, front_tab='', verticalize=False):
	if verticalize:
		if len(m.shape) == 1:
			m = np.atleast_2d(m).T

	out_str = front_tab + str(m).replace('\n ','\n' + front_tab).replace('[[','[').replace(']]',']') + '\n'
	return out_str

def block_two_string_concatenate(str1, str2, spacing='\t'):
	L1 = str1.split('\n')
	L2 = str2.strip().split('\n')

	if len(L1) > len(L2):
		Δ = len(L1) - len(L2)
		for ι in range(Δ):
			L2.append('\n')

	max_width = len(max(L1, key=len))
	outS = ''
	for l1, l2 in zip(L1,L2):
		outS += ('%-' + str(max_width) + 's' + spacing + l2 + '\n') % l1

	return outS


def block_string_concatenate(strList, spacing='\t'):
	outStr = ''
	for single_block in strList:
		if outStr == '':
			outStr = single_block
		else:
			outStr = block_two_string_concatenate(outStr, single_block, spacing=spacing)



if __name__ == "__main__":
	str1 = 'Hello world\nA interesting string'
	str2 = 'Second Block\nto the right\nTooLong'
	outS = block_string_concatenate(str1, str2)
	print(outS)
