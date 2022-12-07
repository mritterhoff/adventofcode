import pp
import heapq as hq
import functools, operator
from functools import cache
from termcolor import colored
import itertools as it

import string
import math
import numpy as np
import copy
from collections import defaultdict, Counter
from parse import *

# p1 27m
# p2 12/5/22 58m

def cost(char):
	return list(string.ascii_uppercase).index(char)+1 + 60
	# return list(string.ascii_uppercase).index(char)+1

f = [x for x in open("input.txt").read().strip().split('\n')]
print(f)

dep = defaultdict(list)
allkeys = set()

for r in f:
	before, after = parse("Step {} must be finished before step {} can begin.", r)
	dep[after].append(before)
	allkeys.add(after)
	allkeys.add(before)

pp(dep)


pp(allkeys)
for k in allkeys:
	if k not in dep:
		dep[k]

# def find_next(path, keys, map):
# 	minLen = 100
# 	foundMe = None
# 	for k in keys:
# 		if len(map[k]) < minLen:
# 			foundMe = k
# 			minLen = len(map[k])
# 		if len(map[k]) == minLen and k < foundMe:
# 			foundMe = k
# 			minLen = len(map[k])
# 	return foundMe

# while len(allkeys) > 0:
# 	foundme = find_next(path, allkeys, dep)
# 	path.append(foundme)
# 	allkeys.remove(foundme)
# 	for k,v in dep.items():
# 		if foundme in v:
# 			v.remove(foundme)

# 	time += 1

def find_next(path, keys, map, status_keys):
	minLen = 10^100
	foundMe = None
	for k in keys:
		if k in status_keys or k in path:
			continue
		if len(map[k]) < minLen:
			foundMe = k
			minLen = len(map[k])
		if len(map[k]) == minLen and k < foundMe:
			foundMe = k
			minLen = len(map[k])
	return foundMe

# map the letter the number of seconds remaining for it, 
# key count maxes at 60

maxWorkers = 5
path = []
status = defaultdict(int)
time = 0

while len(allkeys) > 0:
	# we keep as many workers busy as possible
	addmore = True
	while addmore:
		foundme = find_next(path, allkeys, dep, status.keys())
		if foundme:
			# returned something that isn't in progress, but need to check it's ok:
			hangups = [x for x in dep[foundme] if x in status.keys()]
			if len(hangups) == 0:
				if len(status) == maxWorkers:
					addmore = False
					print("workers maxed out")
				else:
					status[foundme] = cost(foundme)
					print('foundme:', foundme)
			else:
				addmore = False
				print('hungup')
				
		else:
			addmore = False
			print("stuck")

	# a second passes 
	popus = []
	for k,v in status.items():
		status[k] -= 1
		if status[k] == 0:
			popus.append(k)
		
	
	# everyone who needs to be popped, is. 
	pp(status)
	print('path', path)
	print('allkeys:',allkeys)
	print('popus:',popus)
	for killme in popus:
		status.pop(killme)
		path.append(killme)
		allkeys.remove(killme)
		for k,v in dep.items():
			if killme in v:
				v.remove(killme)
	time += 1
	print('time:',time)

pp(allkeys)
rez = "".join(path)

# print("p1:",rez,rez == "GRTAHKLQVYWXMUBCZPIJFEDNSO")
print(time, rez)


# 678 GRTZAHVLQKMXYCIPUWEBJDFNSO
# 687 GRTZAHVLQKMXYCIPUWEBJDFNSO 
# 747 is too low

