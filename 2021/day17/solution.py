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

f = [x for x in open("input.txt").read().strip().split('\n')][0]

xs, ys = f[13:].split(', ')

xbs = [int(x) for x in xs[2:].split('..')]
ybs = [int(y) for y in ys[2:].split('..')]

xrange = range(xbs[0], xbs[1]+1)
yrange = range(ybs[0], ybs[1]+1)
lowerright = (xbs[1], ybs[0])

print(xs,ys)

def getvxdiff(vx):
	if vx == 0:
		return 0
	elif vx > 0:
		return -1
	else:
		return 1


# need to make a function that maps tx,ty to mx over some reasonable range,
# run it for each one, and then find the max

# this should return every position, we'll get the max returned,
# if lower or the right of bounding box, we break
def simulate(tx,ty, xrange, yrange, lowerright):
	px = py = 0
	ps = [(px,py)]
	vx = tx
	vy = ty
	while px <= lowerright[0] and py >= lowerright[1]:
		px += vx
		py += vy
		vx += getvxdiff(vx)
		vy -= 1

		ps.append((px,py))
		if px in xrange and py in yrange:
			return True, ps
	return False, ps

maxh = 0
besttraj = None
cnt = 0
for tx in range(1, 1000):
	for ty in range(-1000, 1000):
		success,ps = simulate(tx, ty, xrange, yrange, lowerright)
		if success:
			cnt += 1
			# localmaxy = max([y for x,y in ps])
			# if localmaxy > maxh:
			# 	besttraj = (tx, ty)
			# 	maxh = localmaxy

print(cnt)
