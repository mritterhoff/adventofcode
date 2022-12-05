import pp
import heapq as hq
import functools, operator
from functools import cache
from termcolor import colored
import itertools as it

import math
import numpy as np
import copy
from collections import defaultdict, Counter
from parse import *

f = [x for x in open("input.txt").read().strip().split('\n')]

# pt1 20m

coords = {}
for ff in f:
	x,y = [int(b) for b in ff.split(', ')]
	coords[len(coords)] = (x,y)

xmin, xmax = min([x for x,y in coords.values()]), max([x for x,y in coords.values()])
ymin, ymax = min([y for x,y in coords.values()]), max([y for x,y in coords.values()])

def mandist(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

def p1_stuff(offset = 1):
	out = {}
	for x in range(xmin-offset, xmax+offset):
		for y in range(ymin-offset, ymax+offset):
			dists = defaultdict(list)
			for co_indx, co in coords.items():
				dists[mandist((x,y), co)].append(co_indx)
			keys = sorted(dists.keys())
			if len(dists[keys[0]]) == 1:
				out[(x,y)] = dists[keys[0]][0]
	return out

summed = defaultdict(int)
for co, pt_index in p1_stuff().items():
	summed[pt_index] += 1

summed2 = defaultdict(int)
for co, pt_index in p1_stuff(10).items():
	summed2[pt_index] += 1

noninf = [summed[k] for k in summed.keys() if summed[k] == summed2[k]]
print('p1:',sorted(noninf)[-1])

offset = 1
out = 0
for x in range(xmin-offset, xmax+offset):
	for y in range(ymin-offset, ymax+offset):
		dist = 0
		for co_indx, co in coords.items():
			dist += mandist((x,y), co)
		if dist < 10000:
			out += 1
print('p2:',out)
