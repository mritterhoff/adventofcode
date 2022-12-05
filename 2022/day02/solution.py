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

# a = complex(2,3)
# b = complex(2,3)
# print(a+b)

# ff = [x.split(',') for x in f]

f = [x for x in open("input.txt").read().strip().split('\n')]
print(f)

ff = [x.split(' ') for x in f]
print(ff)


map = {
	'X': 'A',  # rock
	'Y': 'B',  # paper
	'Z': 'C'   # scisors 
}

score = 0
for r in ff:
	op = r[0]
	me = map[r[1]]

	if me == 'A':
		score += 1
	elif me == 'B':
		score += 2
	else:
		score += 3

	if op == me:
		score += 3
	else:
		if op == 'A' and me == 'B':
			score += 6
		if op == 'A' and me == 'C':
			score += 0
		if op == 'B' and me == 'C':
			score += 6
		if op == 'B' and me == 'A':
			score += 0
		if op == 'C' and me == 'A':
			score += 6
		if op == 'C' and me == 'B':
			score += 0

print('part 1:', score)


# x i lose
# y I draw
# z I win

score = 0
for r in ff:
	op = r[0]
	me = r[1]

	if me == 'X':
		score += 0
		if op == 'A':
			score += 3 #c
		if op == 'B':
			score += 1 #a
		if op == 'C':
			score += 2 #b
	elif me == 'Y':
		score += 3
		if op == 'A':
			score += 1 
		if op == 'B':
			score += 2 
		if op == 'C':
			score += 3 
	else:
		score += 6
		if op == 'A':
			score += 2 
		if op == 'B':
			score += 3 
		if op == 'C':
			score += 1 

print('part 2:', score)

