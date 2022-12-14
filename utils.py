import math
import copy
import string
import pp
import heapq as hq
import functools, operator
from functools import cache, reduce
from termcolor import colored
import itertools as it
import numpy as np
from collections import defaultdict, Counter, deque
from parse import *
from functools import cmp_to_key

import sys
sys.setrecursionlimit(100000)

np.set_printoptions(linewidth=np.inf)
inf = float("inf")

# Return 2-d neighbors of point (as pair) with bounds.
def ns4RC(p, R, C):
	dirs = [(1,0), (-1,0), (0,1), (0,-1)]  # up/down/right/left
	return [(p[0]+dr, p[1]+dc) for dr,dc in dirs if 0<= p[0]+dr < R and 0<= p[1]+dc < C]

def ns8RC(p, R, C):
	dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)] # all 8 neighbors
	return [(p[0]+dr, p[1]+dc) for dr,dc in dirs if 0<= p[0]+dr < R and 0<= p[1]+dc < C]

# Return 2-d neighbors of point (as pair) with bounds.
def ns4XY(p, maxX, maxY):
	dirs = [(1,0), (-1,0), (0,1), (0,-1)]  # right/left/up/down
	return [(p[0]+dx, p[1]+dy) for dx,dy in dirs if 0<= p[0]+dx < maxX and 0<= p[1]+dy < maxY]

def ns8XY(p, maxX, maxY):
	dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)] # all 8 neighbors
	return [(p[0]+dx, p[1]+dy) for dx,dy in dirs if 0<= p[0]+dx < maxX and 0<= p[1]+dy < maxY]



# 2d tiling of a 2d array, with optional lambda for mutation
def tileArray(arr, horiz, vert, permuteLambda = lambda aIn,h,v: aIn):
	out = []	
	for v in range(vert):		
		for h in range(horiz):
			newTile = permuteLambda(arr, h, v)
			if h == 0: newArrayRow = newTile
			else: newArrayRow = np.concatenate((newArrayRow, newTile), axis=1)
		if v == 0: out = newArrayRow
		else: out = np.concatenate((out, newArrayRow), axis=0)
	return out

def sign(v):
	return int((v)/abs(v))

def manDist(t1, t2):
	return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])

def addTupes(t1, t2):
	return (t1[0] + t2[0], t1[1] + t2[1])