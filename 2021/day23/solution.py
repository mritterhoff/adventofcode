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


f = [x for x in open("test.txt").read().strip().split('\n')]

costs = {
	'A': 1,
	'B': 10,
	'C': 100,
	'D': 1000
}

# phase is in 4 parts:
# 0 unmoved
# 1 first move, must keep moving till stopped
# 2 only stop outside of pockets
# 3 moving back towards pockets, keep moving
# 4 back in a pocket 


# 0->1 only if you have available moves
# 1   only one in this phase at a time, you can travel anywhere in hallway (except cantstops)
# 2 	
# 3 	only one in this phase at a time, can only end when in pocket (deep as possible)
# 4 

def whoinphase(phase, states):
	return [s for s in states if s['phase' == phase]]

# def isdone(states):

# returns who we can move, and if empty, if we're success or failure
def whotomove(states):
	poss = whoinphase(3, states)
	if poss: return (poss, None)
	
	poss = whoinphase(1, states)
	if poss: return (poss, None)

	poss0 = [p for p in whoinphase(0, states) if len(possmoves(p['pos'], states)) > 0]
	poss2 = [p for p in whoinphase(2, states) if len(possmoves(p['pos'], states)) > 0]
	combined = [*poss0, *poss2]
	if combined: return (combined, None)

	# otherwise we can't move anyone, so are we successful or not?
	if all([s['phase'] == 4 for s in states]):
		return ([], True)
	return ([], False)



states = []

# id, letter, pos, phase, moves?
def makeobj(char, pos, phase=0, moves=0):
	keys = ['id', 'char', 'pos', 'phase', 'moves']
	values = [len(states), char, pos, phase, moves]
	return dict(zip(keys, values))

m = []

R = len(f)
C = len(f[0])

lets = 'A,B,C,D'.split(",")

for r in range(R):
	line = []
	for c in range(C):
		if c < len(f[r]):
			x = f[r][c]
			if x in ['#', ' ']: x = '#'
			if x == '.': x = ' '
			if x in lets: 
				states.append(makeobj(x, (c,r)))
				x = ' '
		else:
			x = '#'
		line.append(x)
	m.append(line)

goals = {
	'A': [(3,3), (3,2)],
	'B': [(5,3), (5,2)],
	'C': [(7,3), (7,2)],
	'D': [(9,3), (9,2)],
}

def isfree(p, states):
	return len([s for s in states if s['pos'] == p]) == 0

def getgoal(s):
	posp = goals[s['char']]
	if isfree(pos[0]):
		return pos[0]
	return pos[1]



for r in range(R):
	line = []
	for c in range(C):
		o = [o for o in states if o['pos'] == (c,r)]
		if len(o) == 1:
			line.append(o[0]['char'])
		else:
			line.append(m[r][c])
	print(line)

def hallway():
	return [(x, 1) for x in range(1,11+1)]

def cantstops():
	return [(3,1), (5,1), (7,1), (9,1)]

def possmoves(p, states):
	c,r = p
	dr = [1,0,-1,0]
	dc = [0,1,0,-1]
	out = []
	for i in range(0,4):
		nr = r + dr[i]
		nc = c + dc[i]
		p = (nc, nr)
		if 0<= nr < R and 0 <= nc < C and m[nr][nc] == ' ' and isfree(p, states):
			out.append(p)
	return out


for s in states:
	print(s)
	ms = possmoves(s['pos'], states)
	print(f'can move {ms}')


print('started')
for i in range(100000):
	a = copy.deepcopy(states) 
print('done')





