from parse import *
from collections import defaultdict
import functools, operator

lines = [x for x in open("test.txt").read().strip().split('\n')]

def splitempties(lines):
	rez = []
	buf = []
	for line in lines:
		if len(line) == 0:
			rez.append(buf)
			buf = []
		else:
			buf.append(line)
	rez.append(buf)
	return rez

p1, p2, p3 = splitempties(lines)

mytix = []
for line in p1:
	m = parse("{}: {}-{} or {}-{}", line)
	if m:
		nums = [int(x) for x in m[1:]]
		mytix.append([m[0], range(nums[0], nums[1]+1), range(nums[2], nums[3]+1)])

rs = []
for r in mytix:
	rs.append(r[1])
	rs.append(r[2])

baddies = []
good_rows = []
for i in range(len(p3)):
	if i == 0: continue
	
	good = True
	ns = [int(x) for x in p3[i].split(',')]
	for n in ns:
		if sum([n in r for r in rs]) == 0:
			baddies.append(n)
			good = False
	if good:
		good_rows.append(ns)

print('part1', sum(baddies))

def all_true(arr):
	if len(arr) == 0: raise 'empty!'
	return len(arr) == sum([x for x in arr if x])

R = len(good_rows)
C = len(good_rows[0])

D = defaultdict(set)
for c in range(C):
	poss = []
	for e in mytix:
		vals = [good_rows[r][c] for r in range(R)]
		vs_in_rs = [(v in e[1] or v in e[2]) for v in vals]
		if all_true(vs_in_rs):
			D[c].add(e[0])

rez = {}
while(len([x for x in D.values() if len(x) > 0]) > 0):
for k,v in D.items():
		if len(v) == 1:
			rez[k] = list(v)[0]
			for s in D.values(): 
				if rez[k] in s: s.remove(rez[k])


mine = p2[-1].split(',')
print('part2',functools.reduce(operator.mul, [int(mine[k]) for k,v in rez.items() if v.startswith('departure')]))
