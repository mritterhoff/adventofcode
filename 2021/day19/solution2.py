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

f = [x for x in open("input.txt").read().strip().split('\n')]

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

# In total, each scanner could be in any of 24 different orientations
# facing positive or negative x, y, or z, 
# and considering any of four directions "up" from that facing.
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

def getseqforF(seq_num, pt):
	return next(itertools.islice(sequence(pt), seq_num, None))	

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
	if len(best) < 12:
		# print('skipping...')
		pass
	else:
		rez = set([subtract(p1,p2) for p1,p2 in best])
		assert len(rez) == 1
		persmap[(i, j)] = [next(iter(rez)), seq]
		print(f'{i}->{j}: best has {len(best)}, k is {seq}, map: {persmap[(i, j)]}\n')



persmap = {
 (0, 13):[(-46, 165, 1167), 9],
 (1, 16):[(-40, -106, 1338), 6],
 (1, 18):[(-77, -46, -1147), 22],
 (1, 22):[(-121, -1279, -38), 14],
 (1, 24):[(-1351, -45, -46), 3],
 (1, 38):[(-5, 1156, 53), 6],
 (2, 11):[(-45, 1108, -77), 4],
 (2, 28):[(1230, -118, -153), 14],
 (3, 30):[(60, -1314, 100), 21],
 (4, 10):[(-58, 128, 1120), 1],
 (4, 17):[(-1246, 80, 72), 9],
 (4, 23):[(-96, 1224, 57), 23],
 (5, 7):[(1076, -32, 46), 15],
 (5, 34):[(-72, 62, -1229), 14],
 (6, 14):[(-139, 106, -1087), 10],
 (6, 19):[(-1335, 9, 91), 14],
 (6, 29):[(-157, -1222, 148), 4],
 (7, 5):[(1076, -46, 32), 15],
 (7, 20):[(7, -53, -1254), 0],
 (7, 25):[(2, 1131, -60), 15],
 (8, 27):[(-32, 1339, 78), 15],
 (9, 21):[(32, -15, 1369), 18],
 (10, 4):[(-128, 1120, -58), 20],
 (10, 24):[(-160, -108, 1139), 8],
 (11, 2):[(77, 1108, 45), 4],
 (11, 13):[(1247, 29, -11), 23],
 (11, 15):[(8, 9, -1139), 16],
 (11, 20):[(-1194, -124, -78), 3],
 (11, 25):[(-10, -119, 1116), 14],
 (12, 17):[(1252, 5, -37), 21],
 (12, 21):[(35, 1191, -164), 8],
 (13, 0):[(-46, 165, -1167), 9],
 (13, 11):[(-11, 29, 1247), 23],
 (13, 26):[(1160, -1, 95), 17],
 (14, 6):[(106, 139, 1087), 8],
 (14, 37):[(111, -1082, 31), 19],
 (15, 11):[(8, -9, -1139), 16],
 (15, 21):[(1227, 37, 138), 2],
 (15, 26):[(-1144, 21, 32), 1],
 (16, 1):[(-1338, 106, -40), 21],
 (16, 37):[(-22, -44, 1179), 0],
 (17, 4):[(-1246, 80, -72), 9],
 (17, 12):[(-37, -5, -1252), 6],
 (17, 19):[(69, -1136, -96), 2],
 (17, 22):[(1181, 104, -78), 4],
 (17, 24):[(-49, 112, 1156), 21],
 (17, 35):[(43, 1274, -167), 17],
 (18, 1):[(-1147, -77, 46), 12],
 (18, 27):[(38, -74, 1207), 20],
 (18, 31):[(1139, -14, -31), 14],
 (19, 6):[(-9, -91, 1335), 5],
 (19, 17):[(69, -96, -1136), 2],
 (19, 23):[(1219, -81, 8), 1],
 (19, 37):[(-14, -1147, 114), 7],
 (20, 7):[(-7, -1254, 53), 13],
 (20, 11):[(-124, -78, 1194), 7],
 (20, 21):[(-170, 1199, -25), 4],
 (21, 9):[(-32, -15, 1369), 18],
 (21, 12):[(-1191, 35, 164), 10],
 (21, 15):[(1227, 138, 37), 2],
 (21, 20):[(25, 1199, 170), 4],
 (21, 32):[(32, 78, -1038), 22],
 (21, 35):[(88, -1050, 84), 15],
 (22, 1):[(1279, 38, 121), 5],
 (22, 17):[(78, 104, -1181), 4],
 (23, 4):[(57, 1224, -96), 23],
 (23, 19):[(81, 8, 1219), 20],
 (23, 33):[(1305, 26, -110), 14],
 (24, 1):[(-45, -46, 1351), 7],
 (24, 10):[(108, -160, -1139), 10],
 (24, 17):[(1156, -112, 49), 6],
 (24, 37):[(105, -1362, 132), 12],
 (25, 7):[(2, 60, -1131), 15],
 (25, 11):[(119, -1116, 10), 5],
 (25, 28):[(1345, 159, -66), 15],
 (26, 13):[(-1, 1160, 95), 17],
 (26, 15):[(-21, 32, -1144), 20],
 (27, 8):[(-32, -78, -1339), 15],
 (27, 18):[(1207, -38, -74), 1],
 (27, 38):[(5, -1238, -2), 17],
 (28, 2):[(118, 153, -1230), 5],
 (28, 25):[(1345, 66, -159), 15],
 (29, 6):[(-148, -1222, 157), 4],
 (29, 30):[(1136, -155, 32), 14],
 (30, 3):[(100, 1314, -60), 6],
 (30, 29):[(155, -32, -1136), 5],
 (31, 18):[(14, 31, -1139), 5],
 (31, 36):[(-47, -1209, 163), 0],
 (32, 21):[(-1038, 32, -78), 12],
 (33, 23):[(-26, 110, -1305), 5],
 (34, 5):[(-62, 1229, 72), 5],
 (35, 17):[(1274, 43, -167), 17],
 (35, 21):[(88, -84, 1050), 15],
 (36, 31):[(47, 163, 1209), 13],
 (37, 14):[(1082, -111, 31), 19],
 (37, 16):[(22, 1179, 44), 13],
 (37, 19):[(-114, -14, -1147), 3],
 (37, 24):[(-1362, -132, 105), 22],
 (38, 1):[(-53, -1156, -5), 21],
 (38, 27):[(-1238, 5, -2), 17]
 }


# 1: (0, 1)
# 2: (0, 1)(1, 4)(4, 2)
# 3: (0, 1)(1, 3)
# 4: (0, 1)(1, 4)

print(persmap)

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
		endwithme = endswith(keys, i)
		startwithcomplete = startswith(endwithme, complete.keys())
		if len(startwithcomplete) > 0:
			# if len(startwithcomplete) == 1:
			# 	# useme = startwithcomplete[0]
			# 	# print(f'just one: {startwithcomplete[0]}')
			# else:
			# 	# print(f'found many: {startwithcomplete}')

			out = [startwithcomplete[0]]

			while out[0][0] != 0:
				# print(f'out is {out}')
				firstpair = out[0]
				mapped = complete[firstpair[0]]
				# print(f'firstpair is {firstpair}')
				# print(f'mapped is {mapped}')
				# add mapped to beg of out
				out = mapped + out
				# print(f'new out is {out}')

			complete[i] = out
			print(f'out is : {out}')
	# pprint.pp(complete)	

pprint.pp(complete)

def recurse(seqs, i, pt):
	thisseq = seqs[i]

	if i == len(seqs) - 1:
		return getseqforF(thisseq, pt)
	else:
		return getseqforF(thisseq, recurse(seqs, i+1, pt))

offsets = {}
# do this in the same order we figured them out:
# print([x for x in complete.keys() if x != 0])
# assert False

for i in [x for x in complete.keys() if x != 0]:
	print(f'offsets to far: {offsets}')
	path = complete[i]
	rez = None
	if len(path) == 1:
		m0, _ = persmap[path[0]]
		rez = m0

	elif len(path) == 2:
		m0,k0 = persmap[path[0]]
		m1,_ = persmap[path[1]]

		#m0 + permute(m1 to k0's)
		permutted = getseqforF(k0, m1)
		mypred = offsets[path[0][1]]
		print("meeee2", mypred)
		rez = add(mypred, permutted)
	else:
		# get all the keys but the last one
		# get the last m
		keys= []
		lastm = None
		for p in path:
			m,k = persmap[p]
			keys.append(k)
			lastm = m
		keys.pop()

		print('keys is',keys, 'lastm is', lastm)

		# m0,k0 = persmap[path[0]]
		# m1,k1 = persmap[path[1]]
		# m2,_ = persmap[path[2]]

		# look at path before the last
		print(f'offsets are: {offsets}')
		print(f'path is: {path}')
		mypred = offsets[path[-2][1]]
		print("meeee3", mypred)

		# rez = m0 + permute(m1 to k0's) + permute(permute(m2 to k1's) to k0's)
		# rez = add(add(m0, getseqforF(k0, m1)), getseqforF(k0, getseqforF(k1, m2)))
		# recurse(keys, 0, lastm)
		rez = add(mypred, recurse(keys, 0, lastm))
		# rez = add(mypred, getseqforF(k0, getseqforF(k1, m2)))

	offsets[i] = rez

pprint.pp(offsets)


# assert False



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
	# print(f'seqs are {seqs}')

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

def manhattan(p1, p2):
	x1,y1,z1 = p1
	x2,y2,z2 = p2
	return abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

out = []



vals = [x for x in offsets.values()]
print(len(vals), vals)
vals.append((0,0,0))
print(len(vals), vals)

for i in vals:
	for j in vals:
		out.append(manhattan(i, j))
print('part2:',max(out))

11079

# build up all of the perspective mappings,
# then permute every scanner's beacons to scanner 0's perspective
# and take all uniuqe beacons in that set.



