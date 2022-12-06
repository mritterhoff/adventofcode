import pp
import heapq as hq
import functools, operator
from functools import cache
from termcolor import colored
import itertools as it

import string
import math
import numpy as np
import copy
from collections import defaultdict, Counter
from parse import *

list(string.ascii_letters)
list(string.ascii_lowercase)
list(string.ascii_uppercase)	


f = [x for x in open("input.txt").read().strip().split('\n')]
print(f)

# take from a set:
list(some_set)[0]

# set intersection
s1.intersection(s2)
s1.issuperset(s2)

# get index and val from list
for idx, val in enumerate(lst):

list = [x for x in 'abcde']
r = [0]
r.extend([1,2,3]) # r is now [0,1,2,3]

complex(2,3)

# np stuff  https://numpy.org/doc/stable/reference/routines.html
np.fliplr(r)
grid = np.full((5, 5), '') # 5 by 5 grid with '' default


# parse several values from a string that's been formatted. :d returns as int, otherwise str.
id, dx, dy = parse("#{:d} @ {:d},{:d}", in)
# or check if match at all:
rez =  parse("#{:d} @ {:d},{:d}", in)
if rez: print(rez[0])


# Dict aka Maps
# get items in sorted order by keys, largest to smallest
pp(sorted(dt.items(), key=lambda x: x[1], reverse=True))

defaultdict(int)
defaultdict(list)

for k,v in some_dict.items():


# Strings

# 2345, 1345, 1245, 1235, 1234
str = '12345'
for i in range(len(str)): print(str[:i] + str[i+1:])



# itertools https://docs.python.org/3/library/itertools.html

# AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD (like a nested for lop)
it.product('ABCD', repeat=2)

# AB AC AD BA BC BD CA CB CD DA DB DC (all possible orderings, no repeats)
it.permutations('ABCD', 2)

# AB AC AD BC BD CD (all combos with no repeats)
it.combinations('ABCD', 2)

# AA AB AC AD BB BC BD CC CD DD (all combos with repeats)
it.combinations_with_replacement('ABCD', 2)



funcs = {
	"forward": lambda x, y, z: [x+z, y],
	"up": lambda x, y, z: [x, y-z],
	"down": lambda x, y, z: [x, y+z]
}
funcs["forward"](0,1,2)


# classes

class Board:
	def __init__(self, arr):
		self.arr = arr

	def __str__(self):
		return "debug info:" + self.array

copy.deepcopy(copy_me)






def neighbors(p):
	x,y = p
	dirs = [(1,0), (-1,0), (0,1), (0,-1)]  # right/left/up/down
	# dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)] # all 8 neighbors
	ns = []
	for dx,dy in dirs:
		if 0<= x+dx < C and 0<= y+dy < R:
			ns.append((x+dx, y+dy))
	return ns

def hextobin(hex):
	m = { '0': '0000',
	'1': '0001',
	'2': '0010',
	'3': '0011',
	'4': '0100',
	'5': '0101',
	'6': '0110',
	'7': '0111',
	'8': '1000',
	'9': '1001',
	'A': '1010',
	'B': '1011',
	'C': '1100',
	'D': '1101',
	'E': '1110',
	'F': '1111'}
	out = ""
	for x in hex: out += m[x]
	return out








