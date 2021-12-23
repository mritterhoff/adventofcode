import pprint
import heapq as hq
import functools, operator
from functools import cache
from termcolor import colored

import math
import numpy as np
import copy
from collections import defaultdict, Counter
from parse import *


# 2 * 3 + (4 * 5)
# 5 + (8 * 3 + 9 + 3 * 4 * 3)
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2


f = [x for x in open("input.txt").read().strip().split('\n')]


# exp is a list
def solve(exp):
	L = len(exp)
	v = solve(exp[0]) if isinstance(exp[0], list) else exp[0]
	op = None
	for i in range(1,L):
		el = exp[i]
		if el in ['*', '+']:
			op = el
		else:
			v2 = solve(el) if isinstance(el, list) else el
			if op == '*':
				v *= v2
			else:
				v += v2
			op = None
	return v



# exp is a list
# in a given level:
# reduce any parens
# then adds
# then times.
def solve2(exp):
	nexp = []
	L = len(exp)
	# solve all the parens
	for i in range(L):
		if isinstance(exp[i], list):
			rez = solve2(exp[i])
			nexp.append(rez)
		else:
			nexp.append(exp[i])

	#now exp is the list and there are no sub list.
	exp = nexp
	L = len(exp)

	# print(f'done with parens, now is: {exp}')
	if L == 1:
		return exp[0]

	# print(f"doing the adds...{exp}")
	# start pointing to the 3rd and go to the end in steps of 2
	for i in range(2, L, 2):
		if exp[i-1] == '+':
			exp[i] = exp[i] + exp[i-2]
			exp[i-1] = None
			exp[i-2] = None

	# remove the Nones 
	exp = [x for x in exp if x != None]
	# print(f'done with adds, now is: {exp}')
	L = len(exp)
	if L == 1:
		return exp[0]

	# start pointing to the 3rd and go to the end in steps of 2
	for i in range(2, L, 2):
		# print(f"i is {i}, exp is {exp}")
		if exp[i-1] == '*':
			# print('here',exp[i], exp[i-2])
			exp[i] = exp[i] * exp[i-2]
			exp[i-1] = None
			exp[i-2] = None

	exp = [x for x in exp if x != None]
	print(f'done with mults, now is: {exp}')
	if len(exp) > 1:
		raise f"oh no we have {exp}"
	elif len(exp) ==1:
		print(exp)
		return exp[0]
	return exp


def isdigit(c):
	return '0' <= c <= '9'

def parse(line, i):
	# first remove all of the useless spaces
	line = [x for x in line if x != ' ']
	
	# if i == 0: print(line)

	L = len(line)
	exp = []
	while i < L:
		c = line[i]
		# print(f"i is {i}, c is {c}")
		if isdigit(c):
			while i+1 < L and isdigit(line[i+1]):
				c += line[i+1]
				i += 1
			exp.append(int(c))
		elif c in ['*', '+']:
			exp.append(c)
		elif c == '(':
			i, exp_n = parse(line, i+1)
			exp.append(exp_n)
		elif c == ')':
			return i, exp
		else:
			raise f"dunno how to deal with {c}"

		i+=1
	return i, exp

out1 = []
out2 = []
for fin in f:
	i, exp = parse(fin, 0)
	# print(exp)
	# print(exp)
	
	v = solve(exp)
	# print(exp, '=', v)
	out1.append(v)

	v = solve2(exp)
	# print(exp, '=', v)
	out2.append(v)

print(sum(out1))
print(sum(out2))


# for line in f:
# 	parse(line)



