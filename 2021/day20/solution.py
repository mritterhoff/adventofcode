import pprint
import heapq as hq
import functools, operator
from functools import cache
from termcolor import colored
import itertools

import math
import numpy as np
import copy
from collections import defaultdict, Counter
from parse import *

# plus 1 on either side
offset = 11
def xrange(pic):
	xs = [p[0] for p,b in pic.items() if b]
	return range(min(xs)-11, max(xs)+12)

def yrange(pic):
	ys = [p[1] for p,b in pic.items() if b]
	return range(min(ys)-11, max(ys)+12)

def printme(pic):
	grid = []
	for r in yrange(pic):
		row = ""
		for c in xrange(pic):
			row += ('#' if pic.get((c,r), False) else '.')
		grid.append(row)
	pprint.pp(grid)


f = [x for x in open("input.txt").read().strip().split('\n')]


def getneighbors(pic, pt):
	out = []
	x,y = pt
	for dy in [-1,0,1]:
		for dx in [-1,0,1]:
			out.append('1' if pic.get((x+dx,y+dy), False) else '0')
	return int("".join(out), 2)


# pt => bool
pic = {}

print(f)

algo = f[0]

R = 0
for i in range(2, len(f)):
	line = f[i]
	for x in range(len(line)):
		if line[x] == '#':
			pic[(x,R)] = True
	R += 1

def crop(pic):
	pic2 = {}
	ys = yrange(pic)
	xs = xrange(pic)
	for y in ys[offset*2+1:-offset*2-1]:
		for x in xs[offset*2+1:-offset*2-1]:
			pic2[(x,y)] = pic.get((x,y), False)
	return pic2


printme(pic)

for gen in range(0,50):
	print(f'gen is {gen}')
	pic2 = {}
	for y in yrange(pic):
		for x in xrange(pic):
			# get the point

			p = (x,y)
			ns = getneighbors(pic, p)
			algolookup = algo[ns] == '#'
			if algolookup:
				pic2[p] = algolookup
	pic = pic2
	
	# printme(pic)
	if gen % 2 == 1:
		pic = crop(pic)


count = 0
for p in pic:
	if pic.get(p, False):
		count += 1
print(count)




