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

class Node:
    def __init__(self, i=0, v=0):
        self.index = i
        self.value = v

    def get_data(self):
        print(f'i: {self.index}, v: {self.value}')



def magnitude(exp):
	pass

def add(x1, x2):
	return [x1, x2]

def isdigit(c):
	return '0' <= c <= '9'

# def explode2(ex, left, d, exploded = False, remains = (0,0)):
# 	if isinstance(ex, int):
# 		if left:
# 			if remains[0] > 0:
# 				print(f'was {ex} going to add {remains[0]}')
# 				ex = ex + remains[0]
# 				remains = (0, remains[1])
# 		if not left:
# 			if remains[1] > 0:
# 				ex = ex + remains[1]
# 				remains = (remains[0], 0)
# 		return exploded, ex, remains

# 	else:
# 		return explode(ex, d, exploded, remains)


# def explode(ex, d, exploded = False, remains = (0,0)):
# 	# print(f"explode called with {ex}, d={d}, exploded={exploded}, right_remain={right_remain}")
	
# 	if d < 3:
# 		exploded, lex, remains = explode2(ex[0], True, d+1, exploded, remains)
# 		ex[0] = lex
# 		exploded, rex, remains = explode2(ex[1], False, d+1, exploded, remains)
# 		ex[1] = rex
# 		return exploded, ex, remains

# 	if d == 3:
# 		if exploded:
# 			rez = (exploded, ex, remains)
# 			# if remains[1] >0:
# 			# 	exploded, lex, remains = explode2(ex[0], True, d+1, exploded, remains)
# 			# 	ex[0] = lex
# 			# 	exploded, rex, remains = explode2(ex[1], False, d+1, exploded, remains)
# 			# 	ex[1] = rex
# 			# 	rez = (exploded, ex, remains)
# 			# else:
# 			# 	rez = (exploded, ex, remains)

# 		else:
# 			# try to explode the left, end up with a left remain
# 			if isinstance(ex[0], list):
# 				left_remain,r = ex[0]
# 				ex[0] = 0
# 				ex[1] += r
# 				rez = (True, ex, (left_remain, remains[1]))
# 			# try to explode the right, end up with a right remain	
# 			elif isinstance(ex[1], list):
# 				l,right_remain = ex[1]
# 				ex[1] = 0
# 				ex[0] += l

# 				rez = (True, ex, (remains[0], right_remain))
# 			else:
# 				rez = (exploded, ex, remains)

# 	# print(f"d is {d}, returning {rez}")
# 	return rez


# TODO iterate through the string and deal with that?
# or just *know* in the ...


# TODODOTOTODOTO
# make a node class, and number them, so we can go back and manipulate?
# but then what to number the new node?






def listify(exp):
	if isinstance(exp, list):
		return listify(exp[0]) + listify(exp[1])
	else:
		return [exp]

# def explode(exp, d=0, listicle):
# 	if isinstance(exp, list):
# 		if d == 3:
			
# 		else:
# 			explode(exp[0],d+1,listicle)
# 			explode(exp[1],d+1,listicle)




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
		print(f'splitted to: {exp}')
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
# exp3 = reduce(exp3)



print(listify(exp3))
# _, exp3, _ = explode(exp3, 0)
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



