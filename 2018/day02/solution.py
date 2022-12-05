from collections import defaultdict
from parse import *

f = [x for x in open("input.txt").read().strip().split('\n')]

global_counts = defaultdict(int)
for ff in f:
	local_counts = defaultdict(int)
	for x in ff: local_counts[x] += 1
	
	if 2 in local_counts.values(): global_counts[2] += 1
	if 3 in local_counts.values(): global_counts[3] += 1
print('p1:', global_counts[2]*global_counts[3])

past = []
for ff in f:
	now = set()
	for i in range(len(ff)):
		now.add(ff[:i-1] + ff[i:])

	for p in past:
		xs = p.intersection(now)
		if len(xs) > 0:
			print('p2:',list(xs)[0])
	past.append(now)
