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

def part1():
	f = [x for x in open("input.txt").read().strip().split('\n')]

	pos = {}
	for l in f:
		o = parse("Player {} starting position: {}", l)
		pos[int(o[0])]  = int(o[1])

	global numrolls
	numrolls = 0
	global die
	die = 0

	def getroll():
		global numrolls
		global die
		
		dsum = 0
		for r in range(0,3):
			dsum += (die % 100)+1
			die += 1
			numrolls += 1

		return dsum

	p1p = pos[1]
	p2p = pos[2]
	p1s = 0
	p2s = 0

	round = 1
	while True:
		p1p = ((p1p + getroll() -1 ) % 10) + 1
		p1s += p1p
		if p1s >= 1000: break

		p2p = ((p2p + getroll() -1) % 10) + 1
		p2s += p2p
		if p2s >= 1000: break

		round += 1

	print('part1', numrolls * min(p2s, p1s))

part1()


