#!/usr/bin/env python


def block_string_concatenate(str1, str2, spacing='\t'):
	L1 = str1.split('\n')
	L2 = str2.split('\n')

	max_width = len(max(L1, key=len))
	outS = ''
	for l1, l2 in zip(L1,L2):
		outS += ('%-' + str(max_width) + 's' + spacing + l2 + '\n') % l1

	return outS

if __name__ == "__main__":
	str1 = 'Hello world\nA interesting string'
	str2 = 'Second Block\nto the right'
	outS = block_string_concatenate(str1, str2)
	print(outS)
