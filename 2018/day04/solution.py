import pp
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
f = sorted(f)

# p1 took 20m-ish
guard_to_total_time = {}
guard_to_hash = defaultdict(int)

start = 0
cur_id = 0
for line in f:
	rez = parse("[{}] Guard #{:d} begins shift", line)
	if rez:
		cur_id = rez[1]
	
	rez = parse("[{} {}:{:d}] falls asleep", line)
	if rez:
		start = rez[2]

	rez = parse("[{} {}:{:d}] wakes up", line)
	if rez:
		end = rez[2]
		if cur_id not in guard_to_total_time:
			guard_to_total_time[cur_id] = defaultdict(int)
		for x in range(start,end):
			guard_to_total_time[cur_id][x] += 1
			guard_to_hash[cur_id] += 1

id = sorted(guard_to_hash.items(), key=lambda x: x[1], reverse=True)[0][0]
item_w_max_v = sorted(guard_to_total_time[id].items(), key=lambda x: x[1], reverse=True)[0]
print('p1:', item_w_max_v[0] * id)

# pt 2 in 2:38
max_id = 0
max_k = 0
max_v = 0
for id, dd in guard_to_total_time.items():
	for a,b in dd.items():
		if b > max_v:
			max_v = b
			max_k = a
			max_id = id

print('p2:',max_id*max_k)














