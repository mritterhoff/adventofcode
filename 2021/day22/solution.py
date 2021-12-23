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
import pdb

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

l = [1,2,3,4]
print([x for x in chunks(l, 2)])
l = [1,2,3,4,5]
print([x for x in chunks(l, 2)])


# assert False


f = [x for x in open("test.txt").read().strip().split('\n')]

#on x=10..12,y=10..12,z=10..12

dirs = []
for l in f:
	state, rest = l.split(' ')
	dimens = rest.split(',')
	outline = [state]
	for d in dimens:
		a = d[0] # xyz
		limits = d[2:].split('..')
		limits = [int(x) for x in limits]
		# print(a, limits)
		outline.extend(limits)
	dirs.append(outline)

pprint.pp(dirs)
   # 0        1  2      3   4      5   6
# state, x min/max, y min/max, z min/max

# total = range(-50, 50+1)
# def overlap(inrange):
# 	least = max(inrange[0], total[0])
# 	most = min(inrange[-1], total[-1])
# 	return range(least, most+1)


# cubes = defaultdict(bool)
# for dir in dirs:
# 	for x in overlap(range(dir[1], dir[2]+1)):
# 		for y in overlap(range(dir[3], dir[4]+1)):
# 			for z in overlap(range(dir[5], dir[6]+1)):
# 				# if -50 <= x <= 50 and -50 <= y <= 50 and -50 <= z <= 50:
# 				cubes[(x,y,z)] = dir[0] == 'on'

# count = 0
# total = range(-50, 50+1)
# for x in total:
# 	for y in total:
# 		for z in total:
# 			if cubes[(x,y,z)]:
# 				count += 1

# print(count)


# need to keep track of state in ranges, detect if there's overlap, (or contains the other)
# if there isn't, add to range
# otherwise, break all the ranges into sub ranges, add the right ones.

# there has to be overlap in all three dimensions otherwise it doesn't matter
# start testing for that now, deal with splitting up cuboids later

   # 0        1  2      3   4      5   6
# state, x min/max, y min/max, z min/max


# def overlap1d(p1, p2):
# 	print(f'checking {p1} vs {p2}')
# 	return False

# def isoverlap3d(b1, b2):
# 	laps = []
# 	for axis in ['x', 'y', 'z']:
# 		if axis == 'x':
# 			laps.append(overlap1d(b1[:2], b2[:2]))
# 		elif axis == 'y':
# 			laps.append(overlap1d(b1[2:4], b2[2:4]))
# 		else:
# 			laps.append(overlap1d(b1[4:6], b2[4:6]))
	# return laps
	

breaks=[set(),set(), set()]
boids = defaultdict(bool)



# assert False



for dir in dirs:
	breaks[0].add(dir[1])
	breaks[0].add(dir[2])
	breaks[1].add(dir[3])
	breaks[1].add(dir[4])
	breaks[2].add(dir[5])
	breaks[2].add(dir[6])

	# breaks[0].add(dir[1])
	breaks[0].add(dir[2]-1)
	# breaks[1].add(dir[3])
	breaks[1].add(dir[4]-1)
	# breaks[2].add(dir[5])
	breaks[2].add(dir[6]-1)

# print(breaks)

xs = sorted(list(breaks[0]))
ys = sorted(list(breaks[1]))
zs = sorted(list(breaks[2]))

print(xs)
print(ys)
print(zs)


def splitup(boid):
	splits = [[],[],[]]
	myxs = [x for x in xs if x in range(dir[1], dir[2]+1)]
	myys = [x for x in ys if x in range(dir[3], dir[4]+1)]
	myzs = [x for x in zs if x in range(dir[5], dir[6]+1)]

	print('boid', boid)
	print(myxs)
	print(myys)
	print(myzs)

	k = boid[1:]  # 139590
	myboid = (k[1]-k[0]+1)*(k[3]-k[2]+1)*(k[5]-k[4]+1)
	print(f'my boid is {myboid}')

	boidsum = 0

	for xxs in chunks(myxs, 2):
		if len(xxs) == 1:
			xxs.append(xxs[0])
		x,xx = xxs
		
		for yys in chunks(myys, 2):
			if len(yys) == 1:
				yys.append(yys[0])
			y,yy = yys
			for zzs in chunks(myzs, 2):
				if len(zzs) == 1:
					zzs.append(zzs[0])
				z,zz = zzs

				print(f'setting {(x,xx, y,yy, z,zz)} to {boid[0] == "on"}')
				boids[(x,xx, y,yy, z,zz)] = boid[0] == 'on'
				boidsum += (k[1]-k[0]+1)*(k[3]-k[2]+1)*(k[5]-k[4]+1)

	print(len(boids))
	print(myboid, boidsum)
	assert False



# assert False
#(-54112, -39298, -85059, -49293, -27449, -50) True

for dir in dirs:
	splitup(dir)


# got 39787219292675
# ans is 590784

#then, go through and combute how many cubes each boid contains

count = 0
for k,v in boids.items():
	if v:
		# print(k,v)
		count += (k[1]-k[0]+1)*(k[3]-k[2]+1)*(k[5]-k[4]+1)

print(count)






	# for x,xx in zip(myxs[:-1], myxs[1:]):
	# 	xx -=1
	# 	for y,yy in zip(myys[:-1], myys[1:]):
	# 		yy -= 1
	# 		for z,zz in zip(myzs[:-1], myzs[1:]):
	# 			zz -= 1
	# 			print(f'setting {(x,xx, y,yy, z,zz)} to {boid[0] == "on"}')
	# 			boids[(x,xx, y,yy, z,zz)] = boid[0] == 'on'
	# 			boidsum += (k[1]-k[0]+1)*(k[3]-k[2]+1)*(k[5]-k[4]+1)

