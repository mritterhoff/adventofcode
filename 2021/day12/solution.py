from pprint import pprint
import math
import numpy as np
import copy
from collections import defaultdict

f =[x for x in open("test.txt").read().strip().split('\n')]
# f = np.asarray([[int(y) for y in x] for x in f])

print(f)

nodes = set()
edges = defaultdict(list)

# .isupper()
# copy.deepcopy(a)
# list1.extend(list2)

def would_have_to_many_smalls(path, n):
	c = defaultdict(int)
	for x in path:
		if x.islower():
			c[x] += 1
	x = n
	if x.islower():
		c[x] += 1

	most_pop = [x for x in c.values() if x > 1]

	rez = True
	if len(most_pop) == 1 and most_pop[0] == 2:
		rez = False

	# print('in whtms:',path, n, rez)
	return rez

for x in f:
	a, b = x.split('-')
	nodes.add(a)
	nodes.add(b)
	edges[a].append(b)
	edges[b].append(a)

print(nodes)
print(edges)


paths = []

# def explore(path):
# 	rez=[]
# 	cur_node = path[-1]

# 	if cur_node == 'end':
# 		return [path]

# 	for n in edges[cur_node]:
# 		if n in path and n.islower():
# 			continue

# 		p = copy.deepcopy(path)
# 		p.append(n)
# 		rez.extend(explore(p))

# 	return rez

def explore(path):
	rez=[]
	cur_node = path[-1]

	if cur_node == 'end':
		return [path]

	for n in edges[cur_node]:
		if n == 'start':
			continue
		if n in path and n.islower() and would_have_to_many_smalls(path, n):
			continue
		p = copy.deepcopy(path)
		p.append(n)
		rez.extend(explore(p))

	return rez


rez = explore(['start'])

print(len(rez))


