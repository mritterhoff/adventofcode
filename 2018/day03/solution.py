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

f = [x for x in open("input.txt").read().strip().split('\n')]

# p1: total time: 7:05
# p2: total time: 13:00 (6m)

d = defaultdict(int)
for i in f:
	id, dx, dy, xlen, ylen = parse("#{:d} @ {:d},{:d}: {:d}x{:d}", i)
	for x in range(xlen):
		for y in range(ylen):
			d[(x+dx, y+dy)] += 1

sum = 0
for x,y in d.items():
	if y > 1:
		sum += 1
print('p1:', sum)


allids = []
d = defaultdict(list)
for i in f:
	id, dx, dy, xlen, ylen = parse("#{:d} @ {:d},{:d}: {:d}x{:d}", i)
	allids.append(id)
	for x in range(xlen):
		for y in range(ylen):
			d[(x+int(dx), y+int(dy))].append(id)

dupes = set()
for x,y in d.items():
	if len(y) > 1:
		for yy in y:
			dupes.add(yy)

for x in allids:
	if x not in dupes:
		print('p2:', x)

