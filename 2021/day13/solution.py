from pprint import pprint
import math
import numpy as np
import copy
from parse import *

f =[x for x in open("input2.txt").read().strip().split('\n')]
print(f)

def fold(grid, axis, val):
	# get the two sub arrays on either side of the split:
	# print('fliping', axis, val))
	print('input grid is', grid.shape)
	if axis == 'x':
		l = grid[:,:val]
		r = grid[:,val+1:]
		l = copy.deepcopy(l)
		r = copy.deepcopy(r)
		r = np.fliplr(r)
		Rl, Cl = l.shape
		Rr, Cr = r.shape
		print(Rl, Cl, Rr, Cr)
		n = np.empty((Rl, Cl), dtype=str)
		for row in range(0, Rl):
			for col in range(0, Cl):
				if '#' in [l[row][col], r[row][col]]:
					n[row][col] = '#'
		return n
	else:
		l = grid[:val,:]
		r = grid[val+1:,:]
		l = copy.deepcopy(l)
		r = copy.deepcopy(r)

		r = np.flipud(r)
		Rl, Cl = l.shape
		Rr, Cr = r.shape
		print(Rl, Cl, Rr, Cr)
		n = np.empty((Rl, Cl), dtype=str)
		for row in range(0, Rl):
			for col in range(0, Cl):
				if '#' in [l[row][col], r[row][col]]:
					n[row][col] = '#'
		return n

split = f.index('') # find the empty line
pts = []
folds = []
for x in f[0:split]:
	pts.append([int(a) for a in x.split(',')])

for x in f[split+1:]:
	r = parse("fold along {}={}", x)
	folds.append((r[0], int(r[1])))

R = max([p[1] for p in pts]) + 1
C = max([p[0] for p in pts]) + 1
print(R,C)

grid = np.empty((R, C), dtype=str)
print(grid)

for p in pts:
	grid[p[1], p[0]] = '#'

for f in folds:
	print('do fold', f, 'shape was', grid.shape)
	grid = fold(grid, f[0], f[1])
	print('fold done, shape is now', grid.shape)

print(grid)
Rl, Cl = grid.shape
for r in range(Rl):
	o = []
	for c in range(Cl):
		if grid[r][c] == '#':
			o.append('#')
		else:
			o.append(' ')
	print(''.join(o))
