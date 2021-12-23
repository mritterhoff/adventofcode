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

print(f)

pos = {}
for l in f:
	o = parse("Player {} starting position: {}", l)
	pos[int(o[0])]  = int(o[1])

print(pos)


def fancyrolls():
	out = defaultdict(int)
	for i in range(1,4):
		for j in range(1,4):
			for k in range(1,4):
				out[sum([i,j,k])] += 1

	return out

rolls = fancyrolls()


scores = defaultdict(int)

uni = defaultdict(int)
p1p = pos[1]
p2p = pos[2]
p1s = 0
p2s = 0

# (p1p, p1s, p2p, p2s)
state_og = (p1p, p1s, p2p, p2s)

uni[state_og] = 1
pprint.pp(uni)

@cache
def pos_calc(ps, move):
	# rez = ps+move
	# while rez > 10:
	# 	rez = rez -10
	# return rez
	return ((ps + move -1 ) % 10) + 1


def dorolls(uni, player):
	uni2 = defaultdict(int)

	for s,cnt in uni.items():
		p1p, p1s, p2p, p2s = s

		for rsum, rcnt in rolls.items():
			if player == 0:
				newpos = pos_calc(p1p, rsum)
				newstate = (newpos, p1s+newpos, p2p, p2s)
				uni2[newstate] += cnt*rcnt
			else:
				newpos = pos_calc(p2p, rsum)
				newstate = (p1p, p1s, newpos, p2s+newpos)
				uni2[newstate] += cnt*rcnt

	return uni2


def doaccounting(uni):
	max_score = 210
	uni2 = defaultdict(int)

	for s,cnt in uni.items():
		p1p, p1s, p2p, p2s = s

		if p1s >= max_score:
			scores[0] += cnt
		elif p2s >= max_score:
			scores[1] += cnt
		else:
			uni2[s] += cnt
	return uni2

# state is initial positions, and then each pair of rolls after that?
# map of state -> universe count, each roll, multiply everything by 27?

round = 1
while len(uni) > 0:

	uni = dorolls(uni, 0)
	# print(len(uni), sum(uni.values()))
	uni = doaccounting(uni)
	# print(len(uni), sum(uni.values()))
	# pprint.pp(uni)

	uni = dorolls(uni, 1)
	# print(len(uni), sum(uni.values()))
	uni = doaccounting(uni)
	# print(len(uni), sum(uni.values()))
	round += 1
	print(round)

print('part2', max(scores.values()))




