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

f = [x for x in open("test.txt").read().strip().split('\n')]
# print(f)

scanners = {}

cur_scanner = []
sc_num = None
for line in f:
	title = parse("--- scanner {} ---", line)
	if title:
		sc_num = int(title[0])
	elif len(line) == 0:
		scanners[sc_num] = cur_scanner
		sc_num = None
		cur_scanner = []
	else:
		el = line.split(',')
		cur_scanner.append(tuple([int(x) for x in el]))
scanners[sc_num] = cur_scanner

# for k,y in scanners.items():
# 	print(k,":",y)

# In total, each scanner could be in any of 24 different orientations
# facing positive or negative x, y, or z, 
# and considering any of four directions "up" from that facing.

# so any of 6 faces could be "up" (-/+)(x,y,z)
# could be rotated any 90* step around that axis 0,90,180,270

# z+ is up, then 0,90,180,270 spinning of x,y
# 3*2*1 = 6
# 2*2*2 = 8

def roll(v): return (v[0],v[2],-v[1])
def turn(v): return (-v[1],v[0],v[2])


def sequence (v):
    for cycle in range(2):
        for step in range(3):  # Yield RTTT 3 times
            v = roll(v)
            yield(v)           #    Yield R
            for i in range(3): #    Yield TTT
                v = turn(v)
                yield(v)
        v = roll(turn(roll(v)))  # Do RTR


def getseqfor(pt, seq_num):
	gen = sequence(pt)
	r = next(itertools.islice(gen, seq_num, None))	
	return r

def getseqforF(seq_num, pt):
	gen = sequence(pt)
	r = next(itertools.islice(gen, seq_num, None))	
	return r

def attempt(g1, g2):
	best_pairs = []
	# for every pair in g1 and g2, assume they are the same point
	# by moving them both to the origin and every other point by that same amount
	# print(f'g1 len is {len(g1)}, g2 len is {len(g2)}')

	for p1 in g1:
		for p2 in g2:
			g1_trans = [tuple([x-p1[0],y-p1[1],z-p1[2]]) for x,y,z in g1]
			g2_trans = [tuple([x-p2[0],y-p2[1],z-p2[2]]) for x,y,z in g2]

			# print(f'shifted {g1[0:2]} by {p1} to get {g1_trans[0:2]}')
			# print(g2_trans)
			# print(p1,p2)
			overlap = list(set(g1_trans) & set(g2_trans))
			if len(overlap) > len(best_pairs):
				p1s = [tuple([x+p1[0],y+p1[1],z+p1[2]]) for x,y,z in overlap]
				p2s = [tuple([x+p2[0],y+p2[1],z+p2[2]]) for x,y,z in overlap]
				best_pairs = list(zip(p1s,p2s))
	return best_pairs

def ptstr(pt):
	x,y,z = pt
	return f"{x},{y},{z}"


def subtract(p1,p2):
	return (p1[0]-p2[0],p1[1]-p2[1],p1[2]-p2[2])

def add(p1,p2):
	return (p1[0]+p2[0],p1[1]+p2[1],p1[2]+p2[2])

def sprint(pairs):
	pprint.pp([ [ptstr(a), ptstr(b)] for a,b in pairs])

def getpermute(l):
	out = defaultdict(list)
	pgroups = []
	for row in l:
		lps = [v for v in sequence(row)]
		for i in range(len(lps)):
			out[i].append(lps[i])
	return out


persmap = {}


def do_stuff(scanners, i, j):
	best = []
	seq = None
	for k,v in getpermute(scanners[j]).items():
		rez = attempt(scanners[i], v)
		if len(rez) > len(best):
			best = rez
			seq = k

	# col1 is sc0 OG. col2 is sc1, rotated to sc1's frame of ref? 
	# sprint(best)
	print(f'found: {len(best)} in best')
	if len(best) < 12:
		# print('skipping...')
		pass
	else:
		rez = set([subtract(p1,p2) for p1,p2 in best])
		assert len(rez) == 1
		persmap[(i, j)] = [next(iter(rez)), seq]
		print(f'{i}->{j}: best has {len(best)}, k is {seq}, map: {persmap[(i, j)]}\n')

# S = len(scanners)
# print(S)
# for i in range(S):
# 	for j in range(S):
# 		if i != j:
# 			do_stuff(scanners,i,j)

# pprint.pp([f'{k}->{v}' for k,v in persmap.items()])

persmap = {
 (0, 1): [(68, -1246, -43), 16],
 (1, 0): [(68, 1246, -43), 16],
 (1, 3): [(160, -1134, -23), 11],
 (1, 4): [(88, 113, -1104), 20],
 (2, 4): [(1125, -168, 72), 19],
 (3, 1): [(-160, 1134, 23), 11],
 (4, 1): [(-1104, -88, 113), 1],
 (4, 2): [(168, -1125, 72), 19],
}

# 1: (0, 1)
# 2: (0, 1)(1, 4)(4, 2)
# 3: (0, 1)(1, 3)
# 4: (0, 1)(1, 4)

# print(persmap)

# need to get a chain of perspective from 0 to n
# where n is everything not 0

def startswith(ps, i):
	if isinstance(i, int):
		i = [i]
	return [x for x in ps if x[0] in i]

def endswith(ps, i):
	if isinstance(i, int):
		i = [i]
	return [x for x in ps if x[1] in i]

keys = persmap.keys()

# This assumes only one way to get to each node, might not hold up.
complete = defaultdict(list)
complete[0].append((0,0))
S = len(scanners)
while len(complete) < S:
	for i in range(1, S):
		if i in complete.keys():
			continue
		print(f'lookin for path to {i}')
		endwithme = endswith(keys, i)
		startwithcomplete = startswith(endwithme, complete.keys())
		if len(startwithcomplete) > 0:
			out = startwithcomplete

			while out[0][0] != 0:
				print(f'out is {out}')
				firstpair = out[0]
				mapped = complete[firstpair[0]]
				print(f'firstpair is {firstpair}')
				print(f'mapped is {mapped}')
				# add mapped to beg of out
				out = mapped + out
					# out.insert(0, complete[firstpair[0]][0])
				print(f'new out is {out}')

			complete[i] = out
	pprint.pp(complete)	

pprint.pp(complete)


# persmap = {
#  (0, 1): [(68, -1246, -43), 16],
#  (1, 0): [(68, 1246, -43), 16],
#  (1, 3): [(160, -1134, -23), 11],
#  (1, 4): [(88, 113, -1104), 20],
#  (2, 4): [(1125, -168, 72), 19],
#  (3, 1): [(-160, 1134, 23), 11],
#  (4, 1): [(-1104, -88, 113), 1],
#  (4, 2): [(168, -1125, 72), 19],
# }

offsets = {}
for i in range(1,S):
	path = complete[i]
	# print(f'\n{i} from perspective of 0 is:')
	# print(f'my path to {i} is {path}')
	rez = None
	if len(path) == 1:
		p0 = path[0]
		m0, _ = persmap[p0]
		rez = m0

	elif len(path) == 2:
		pass
		m0,k0 = persmap[path[0]]
		m1,_ = persmap[path[1]]

		#m0 + permute(m1 to k0's)
		rez = add(m0, getseqforF(k0, m1))
	else:
		m0,k0 = persmap[path[0]]
		m1,k1 = persmap[path[1]]
		m2,_ = persmap[path[2]]

		# rez = m0 + permute(m1 to k0's) + permute(permute(m2 to k1's) to k0's)
		rez = add(add(m0, getseqforF(k0, m1)), getseqforF(k0, getseqforF(k1, m2)))

		rez = add(add(
			m0, 
			getseqforF(k0, m1)), 
			getseqforF(k0, getseqforF(k1, m2)))

	# print(rez)
	offsets[i] = rez

pprint.pp(offsets)

def recurse(seqs, i, pt):
	thisseq = seqs[i]

	if i == len(seqs) - 1:
		return getseqforF(thisseq, pt)
	else:
		return getseqforF(thisseq, recurse(seqs, i+1, pt))


def transformToSc0FOR(snum):
	path = complete[snum]
	print(snum, path)

	offset = offsets[snum]
	out = []

	# get all the seqs:
	seqs = []
	for p in path:
		k,v = persmap[p]
		seqs.append(v)
	print(f'seqs are {seqs}')

	for p in scanners[snum]:
		trans = recurse(seqs, 0, p)
		out.append(add(offset, trans))
	
	return out

allpoints = set()
for s in range(S):
	if s == 0:
		allpoints.update(scanners[0])
	else:
		allpoints.update(transformToSc0FOR(s))

print(len(allpoints))



# build up all of the perspective mappings,
# then permute every scanner's beacons to scanner 0's perspective
# and take all uniuqe beacons in that set.



































# seq_num = 11 is the identity
# print(p, getseqfor(p,11))

# assert False

# (0,0,1,0)
# facesup = [
# 	(1,0,0),
# 	(-1,0,0),
# 	(0,1,0),
# 	(0,-1,0),
# 	(0,0,1),
# 	(0,0,-1),
# ]
# facesup = [
# 	lambda x,y,z : (-z,y,x),  # x is up  x,z -z x
# 	lambda x,y,z : (z,y,-x),  # x is down

# 	lambda x,y,z : (x,-z, y),  # y is up  y,z -z, y
# 	lambda x,y,z : (-x,z, y),  # y is down

# 	lambda x,y,z : (x,y,z),  # z is up
# 	lambda x,y,z : (-x,y,-z),  # z is down
# ]
# # given a,b they return:
# rotes = [
# 	lambda a, b : (a, b),
# 	lambda a, b : (-b, a),
# 	lambda a, b : (-a, -b),
# 	lambda a, b : (b, -a),
# ]
# (1-6, 1-4)

# look at scanner 1
# pgroups = []
# for fu in facesup:
# 	for r in rotes:
# 		npgroups = []
# 		for row in scanners[1]:
# 			x,y,z = fu(*row)
# 			nrow = [*r(x,y),z]
# 			# print(f'{row} -> {tuple(nrow)}')
# 			npgroups.append(tuple(nrow))
# 		pgroups.append(sorted(npgroups))
