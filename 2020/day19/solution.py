#https://adventofcode.com/2020/day/19

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

f = open("test.txt").read().strip()

rules, messages = f.split('\n\n')

# print(rules, messages)

R = {}
for rule in rules.split('\n'):
	m = parse('{}: "{}"', rule)
	print(m)
	if m:
		R[int(m[0])] = m[1]
	else:
		m = parse('{}: {}', rule)
		ds = [x.strip() for x in m[1].split('|')]
		ds = [x.split(' ') for x in ds]
		out = []
		for d in ds:
			out.append(tuple([int(x) for x in d]))

		R[int(m[0])] = out


print(R)
print(messages)



done = {}

for k,v in R.items():
	if isinstance(v, str):
		done[k] = v
		R[k] = None

print(done)


# def join(l):
# 	if len(l) == 1:
# 		return l[0]

# 	out = []
# 	me = l[0]
# 	for x in join(l[1:]):
# 		mex = [me]
# 		mex.append(x)

# 		out.append(mex)
# 	return out

def prefixer(prefix, rest, i)
	# if we're at the last element...
	if len(rest) == i-1:
		if isinstance(rest, list):
			return [prefix+x for x in rest]
		else:
			return [prefix+x]

	return prefixer(prefix+rest)

# it doesn't get that deep:
# {0: [(4, 1, 5)], 1: [(2, 3), (3, 2)], 2: [(4, 4), (5, 5)], 3: [(4, 5), (5, 4)], 4: 'a', 5: 'b'}
so 
def getsubs(listoftups, done):
	out = []
	for tup in listoftups:
		tuprules = []
		for e in tup:
			emapped = done[e]
			tuprules.append(emapped)

		# now this is some cobmobo of strings and array of strings, like:
		# a, b, [ab, bb] which we want to return:
		# abab, abbb
		for rez in prefixer("", tuprules, 0):
			out.append(rez)

	return out


i = 0
while len(R) > 0 and i < 100:
	pprint.pp(f'done is {done}')
	i += 1
	for k,llr in R.items():
		if not llr:
			continue
		# get all the ints in v:
		set_of_rules = set()
		for lr in llr:
			for r in lr:
				set_of_rules.add(r)
		print(f'set_of_rules {set_of_rules}')

		# check if all the rules referenced are done
		# assuming that all of the rules reference in llr are done at once.
		if len(set_of_rules) == len(set(set_of_rules) & set(done.keys())):
			print(f'set_of_rules {set_of_rules} is in done {done.keys()}')
		
			R[k] = None
			done[k] = getsubs(llr, done)


# this isn't right, prably need to make it some function that takes a list of lists,
# returns a combo of all of them if there's more than one in it
# {4: 'a',
#  5: 'b',
#  2: ['a', 'a', 'b', 'b'],
#  3: ['a', 'b', 'b', 'a'],
#  1: ['aabb', 'abba', 'abba', 'aabb'],
#  0: ['a', 'aabbabbaabbaaabb', 'b']}

pprint.pp(done)











