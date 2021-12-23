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

f = [x for x in open("test.txt").read().strip().split('\n')]


def magnitude(exp):
	pass

def add(x1, x2):
	return [x1, x2]

def isdigit(c):
	return '0' <= c <= '9'

def explode(ex, d, exploded = False, remain = 0):
	# print(f"explode called with {ex}, d={d}, exploded={exploded}, remain={remain}")
	if isinstance(ex, int):
		ex = ex + remain
		# exploded, ex, remain
		return exploded, ex, min(0, remain)

	if d < 3:
		exploded, lex, remain = explode(ex[0], d+1, exploded, remain)
		ex[0] = lex
		exploded, rex, remain = explode(ex[1], d+1, exploded, remain)
		ex[1] = rex
		return exploded, ex, remain

	if d == 3:
		if exploded:
			if remain >0:
				exploded, lex, remain = explode(ex[0], d+1, exploded, remain)
				ex[0] = lex
				exploded, rex, remain = explode(ex[1], d+1, exploded, remain)
				ex[1] = rex
				rez = (exploded, ex, remain)
			else:
				rez = (exploded, ex, remain)

		else:
			if isinstance(ex[0], list):
				l,r = ex[0]
				ex[0] = 0
				ex[1] += r
				rez = (True, ex, remain)
			elif isinstance(ex[1], list):
				l,r = ex[1]
				ex[1] = 0
				ex[0] += l

				rez = (True, ex, r)
			else:
				rez = (exploded, ex, remain)

	# print(f"d is {d}, returning {rez}")
	return rez

def split(ex, done = False):
	if isinstance(ex, int):
		if not done and ex > 9:
			done = True
			return [ex // 2, round(ex/2)], done
		return ex, done

	lex, done = split(ex[0], done)
	ex[0] = lex
	rex, done = split(ex[1], done)
	ex[1] = rex
	return ex, done


def reduce(exp):
	exploded = True
	
	# if you exploded once, try again:
	while exploded:
		exploded, exp, _ = explode(exp, 0)
		if exploded: print(f'exploded to: {exp}')

	exp, splited = split(exp)


	if splited:
		print(f'splited to: {exp}')
		exp = reduce(exp)
	return exp





def parse(line, i):
	L = len(line)
	exp = []
	while i < L:
		c = line[i]
		if isdigit(c):
			exp.append(int(c))
		elif c == '[':
			i, exp_n = parse(line, i+1)
			exp.append(exp_n)
		elif c == ']':
			return i, exp
		elif c == ',':
			pass
		else:
			print(f"dunno how to deal with {c}")
			raise 'oh no'

		i+=1
	return i, exp

def qparse(exp):
	rez = parse(exp, 0)[1][0]
	if len(rez) == 1:
		return rez[0]
	return rez

exp1 = qparse('[[[[[4,3],4],4],[7,[[8,4],9]]]')
print(exp1)
# print(len(exp1))
exp2 = qparse('[1,1]')
# print(len(exp2))
print(exp2)

exp3 = add(exp1, exp2)
print(exp3)
exp3 = reduce(exp3)
print(exp3)

# exp4 = reduce(exp3)
# print(exp4)

# _, exp, _ = explode(exp, 0)
# print(exp)

# exp = qparse('[9,9]')
# print(exp)
# ex, _ = split(exp)
# print(exp)

# v = None
# for exp in f:
# 	exp = parse(exp)
# 	if v == None:
# 		v = exp
# 	else:
# 		v = add(v, exp)

# print(v)



