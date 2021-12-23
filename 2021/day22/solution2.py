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

# def chunks(lst, n):
#     """Yield successive n-sized chunks from lst."""
#     for i in range(0, len(lst), n):
#         yield lst[i:i + n]

# l = [1,2,3,4]
# print([x for x in chunks(l, 2)])
# l = [1,2,3,4,5]
# print([x for x in chunks(l, 2)])


# compare inclusive range r1 and r2:
# 
# part - there is some overlap
# none - there is no overlap at all
# r1insider2
# r2insider1

debug = False

def tupify(x):
	return x if type(x) is tuple else tuple(x)

def qrange(l):
	return range(l[0], l[1]+1)

def engulf(r1, r2):
	r1s, r1e = r1
	r2s, r2e = r2
	justr2 = None
	# figure out what the parts that are only r2 are
	if r1s == r2s:
		#begnnings are the same
		justr2 = (r1e+1, r2e)
	elif r1e == r2e:
		# ends are the same
		justr2 = (r2s, r1s-1)
	else:
		# it's a bit easier
		justr2 = [(r2s, r1s-1), (r1e+1, r2e)]
	return [None, tupify(r1), justr2]


def partial(r1, r2):
	r1s, r1e = r1
	r2s, r2e = r2
	return [(r1s, r2s-1), (r2s, r1e), (r1e+1, r2e)]



# these are both len 2 lists
def compare(r1, r2):
	r1 = tupify(r1)
	r2 = tupify(r2)
	r1s, r1e = r1
	r2s, r2e = r2
	print(f'compare {r1}, {r2}')

	r1r = qrange(r1)
	r2r = qrange(r2)

	if r1r == r2r:
		if debug: print(f'r1 {r1} is the same as {r2}')
		return [None, r1, None]

	if r1s in r2r and r1e in r2r:
		if debug: print(f'r1 {r1} completely in r2 {r2}')
		return engulf(r1, r2)

	if r2s in r1r and r2e in r1r:
		if debug: print(f'r1 {r1} completely around r2 {r2}')
		return list(reversed(engulf(r2, r1)))

	# from here on, it's partial or not at all
	if r1e in r2r and r2s in r1r:
		if debug: print(f'r1 {r1} partially overlaps with r2 {r2} way 1')
		return partial(r1, r2)
	if r1s in r2r and r2e in r1r:
		if debug: print(f'r1 {r1} partially overlaps with r2 {r2} way 2')
		return list(reversed(partial(r2, r1)))


	if debug: print(f'r1 {r1} does not overlap with r2 {r2}')
	return [r1, None, r2]

# r1 = [3,4]
# r2 = [1,5]
# print(compare(r1, r2))
# print(compare(r2, r1))
# print(compare([0,5], [5,10]))
# print(compare([0,5], [3,10]))
# print(compare([5,10], [0,5]))
# print(compare([3,10], [0,5]))
# print(compare([3,10], [11,12]))
# print(compare([11,12], [3,10]))

# assert False



f = [x for x in open("test.txt").read().strip().split('\n')]



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

# pprint.pp(dirs)
   # 0        1  2      3   4      5   6
# state, x min/max, y min/max, z min/max



# def splitup(boid):
# 	splits = [[],[],[]]
# 	myxs = [x for x in xs if x in range(dir[1], dir[2]+1)]
# 	myys = [x for x in ys if x in range(dir[3], dir[4]+1)]
# 	myzs = [x for x in zs if x in range(dir[5], dir[6]+1)]

# 	print('boid', boid)
# 	print(myxs)
# 	print(myys)
# 	print(myzs)

# 	k = boid[1:]  # 139590
# 	myboid = (k[1]-k[0]+1)*(k[3]-k[2]+1)*(k[5]-k[4]+1)
# 	print(f'my boid is {myboid}')

# 	boidsum = 0

# 	for xxs in chunks(myxs, 2):
# 		if len(xxs) == 1:
# 			xxs.append(xxs[0])
# 		x,xx = xxs
		
# 		for yys in chunks(myys, 2):
# 			if len(yys) == 1:
# 				yys.append(yys[0])
# 			y,yy = yys
# 			for zzs in chunks(myzs, 2):
# 				if len(zzs) == 1:
# 					zzs.append(zzs[0])
# 				z,zz = zzs

# 				print(f'setting {(x,xx, y,yy, z,zz)} to {boid[0] == "on"}')
# 				boids[(x,xx, y,yy, z,zz)] = boid[0] == 'on'
# 				boidsum += (k[1]-k[0]+1)*(k[3]-k[2]+1)*(k[5]-k[4]+1)

# 	print(len(boids))
# 	print(myboid, boidsum)
# 	assert False


# todo maintain diff generations of cubes


cubes = set()
for dir in dirs[0:2]:
	cubes2 = set()
	tcube = tuple(dir[1:])
	print('tcube is ', tcube)

	turnon = dir[0] == 'on'

	if len(cubes) == 0 and turnon:
		cubes2.add(tcube)
	else:
		newcubes =[tcube]

		while len(newcubes) > 0:
			print(f'newcubes length is {len(newcubes)}')

			newcube = newcubes.pop(0)
			# compare the cube we're tying to add to... every other cube.
			# if every dimen has some overlap, do the work
			# which probably involves removing both cubes, breaking them all up
			# then adding the postive leftovers back, if there is any
			# but if not overlapping in every dimen, move on
			overlap_free = True
			for existingcube in cubes:
				if debug: print(f'looking at {existingcube} vs {newcube}')
				xover = compare(existingcube[0:2], newcube[0:2])
				yover = compare(existingcube[2:4], newcube[2:4])
				zover = compare(existingcube[4:], newcube[4:])
				dims = [xover, yover, zover]
				for over in dims:
					print(over)

				nolaps = all(not laps for (_, laps, _) in dims)
				if nolaps:
					print('there are no overlaps for the combo {existingcube} and {newcube}')
					cubes2.add(existingcube)
				else:
					overlap_free = False

					# the 1st and 3rd term of each dimen overlap array COULD be
					# a list of 2 tuples, rather than just a tuple
					print('there are overlaps!')
					pprint.pp(dims)
					
					# {existingcube} vs {newcube}
					if any(any(isinstance(o,list) for o in dim) for dim in dims):
						print(f'{dims} has a list in it! stopping')
						assert False

					# no lists, so this is easy, ish.
					if turnon:
						# we only need to add the right most R's:
						newcubes.apped()

					assert False

			# if there wer no over laps, we didn't do any of the above, can just simply add the new cube
			if overlap_free and turnon:
				cubes2.add(tcube)

	print(f'there are {len(cubes2)} in cubes2')
	cubes = cubes2





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


# what if each was a chunk of 100 points, and if it was all true or false, cool, otherwise
# keep track of a sub dict with the true positions. 


# breaks=[set(),set(), set()]
# boids = defaultdict(bool)



# # assert False



# for dir in dirs:
# 	breaks[0].add(dir[1])
# 	breaks[0].add(dir[2])
# 	breaks[1].add(dir[3])
# 	breaks[1].add(dir[4])
# 	breaks[2].add(dir[5])
# 	breaks[2].add(dir[6])

# 	# breaks[0].add(dir[1])
# 	breaks[0].add(dir[2]-1)
# 	# breaks[1].add(dir[3])
# 	breaks[1].add(dir[4]-1)
# 	# breaks[2].add(dir[5])
# 	breaks[2].add(dir[6]-1)

# # print(breaks)

# xs = sorted(list(breaks[0]))
# ys = sorted(list(breaks[1]))
# zs = sorted(list(breaks[2]))

# print(xs)
# print(ys)
# print(zs)


# def splitup(boid):
# 	splits = [[],[],[]]
# 	myxs = [x for x in xs if x in range(dir[1], dir[2]+1)]
# 	myys = [x for x in ys if x in range(dir[3], dir[4]+1)]
# 	myzs = [x for x in zs if x in range(dir[5], dir[6]+1)]

# 	print('boid', boid)
# 	print(myxs)
# 	print(myys)
# 	print(myzs)

# 	k = boid[1:]  # 139590
# 	myboid = (k[1]-k[0]+1)*(k[3]-k[2]+1)*(k[5]-k[4]+1)
# 	print(f'my boid is {myboid}')

# 	boidsum = 0

# 	for xxs in chunks(myxs, 2):
# 		if len(xxs) == 1:
# 			xxs.append(xxs[0])
# 		x,xx = xxs
		
# 		for yys in chunks(myys, 2):
# 			if len(yys) == 1:
# 				yys.append(yys[0])
# 			y,yy = yys
# 			for zzs in chunks(myzs, 2):
# 				if len(zzs) == 1:
# 					zzs.append(zzs[0])
# 				z,zz = zzs

# 				print(f'setting {(x,xx, y,yy, z,zz)} to {boid[0] == "on"}')
# 				boids[(x,xx, y,yy, z,zz)] = boid[0] == 'on'
# 				boidsum += (k[1]-k[0]+1)*(k[3]-k[2]+1)*(k[5]-k[4]+1)

# 	print(len(boids))
# 	print(myboid, boidsum)
# 	assert False



# # assert False
# #(-54112, -39298, -85059, -49293, -27449, -50) True

# for dir in dirs:
# 	splitup(dir)


# # got 39787219292675
# # ans is 590784

# #then, go through and combute how many cubes each boid contains

# count = 0
# for k,v in boids.items():
# 	if v:
# 		# print(k,v)
# 		count += (k[1]-k[0]+1)*(k[3]-k[2]+1)*(k[5]-k[4]+1)

# print(count)






	# for x,xx in zip(myxs[:-1], myxs[1:]):
	# 	xx -=1
	# 	for y,yy in zip(myys[:-1], myys[1:]):
	# 		yy -= 1
	# 		for z,zz in zip(myzs[:-1], myzs[1:]):
	# 			zz -= 1
	# 			print(f'setting {(x,xx, y,yy, z,zz)} to {boid[0] == "on"}')
	# 			boids[(x,xx, y,yy, z,zz)] = boid[0] == 'on'
	# 			boidsum += (k[1]-k[0]+1)*(k[3]-k[2]+1)*(k[5]-k[4]+1)

