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

class Node:
    def __init__(self, v=0, i=0):
        self.value = v
        self.index = i

    def get_data(self):
        print(f'i: {self.index}, v: {self.value}')

    def __repr__(self):
        return f'{self.value}'
        # return f'{self.value} ({self.index})'

# n = Node(1,2)
# print(n)
# n.value = 10
# print(n)


def magnitude(exp):
	if isinstance(exp, list):
		l = magnitude(exp[0])
		r = magnitude(exp[1])
		return 3*l + 2*r
	else:
		return exp.value


def add(x1, x2):
	exp = [x1, x2]
	renumber(exp)  # FUUUUUUUU
	return exp

def parse(line, i=0):
	L = len(line)
	exp = []
	while i < L:
		c = line[i]
		if '0' <= c <= '9':
			exp.append(Node(int(c)))
		elif c == '[':
			i, exp_n = parse(line, i+1)
			exp.append(exp_n)
		elif c == ']':
			return i, exp
		elif c == ',':
			pass
		else:
			raise 'oh no'

		i+=1
	return i, exp

# depths
def ds(ex, d=0):
	if isinstance(ex, list):
		l = ds(ex[0], d+1)
		r = ds(ex[1], d+1)
		return l + r
	else:
		return [d]

# values
def vs(ex):
	if isinstance(ex, list):
		l = vs(ex[0])
		r = vs(ex[1])
		return l + r
	else:
		return [ex.value]


# return ex, remains
def get_explodee(ex, d=0):
	# print(f'get_explodee called with {ex} - {d}')

	if isinstance(ex, Node):
		return ex, None
	if d < 3:
		lex, remains = get_explodee(ex[0], d+1)
		
		# remains mean we done
		if remains:
			ex[0] = lex
			return ex, remains
		else:
			rex, remains = get_explodee(ex[1], d+1)
			if remains:
				ex[1] = rex
				return ex, remains
		return ex, None
		
	else:
		if isinstance(ex[0], list):
			# print(f'EXPLODING {ex[0]}')
			remains = ex[0]
			ex[0] = Node(0, -100)
			return ex, remains

		if isinstance(ex[1], list):
			# print(f'EXPLODING {ex[1]}')
			remains = ex[1]
			ex[1] = Node(0, -100)
			return ex, remains

		return ex, None

def apply_explodee(ex, remains):
	if not remains:
		return
	if isinstance(ex, list):
		apply_explodee(ex[0], remains)
		apply_explodee(ex[1], remains)
	else:
		# print(f'ex: {ex}, remains: {remains}')
		if ex.index == remains[0].index - 1:
			ex.value += remains[0].value
		elif ex.index == remains[1].index + 1: 
			ex.value += remains[1].value

def renumber(exp, count=0):
	if isinstance(exp, list):
		count = renumber(exp[0], count)
		count = renumber(exp[1], count)
		return count
	else:
		exp.index = count
		return count+1

# returns exp, done
def split(exp, done = False):
	if isinstance(exp, Node):
		if done:
			return exp, done
		else: 
			if exp.value > 9:
				nexp = [Node(exp.value // 2, -100), Node(math.ceil(exp.value/2), -100)]
				# print(f'SPLITTING {exp.value} => {nexp}')
				if nexp[0].value + nexp[1].value != exp.value:
					raise "WE FUCKED UP"
				return nexp, True
			else:
				return exp, done
	else:	
		lexp, done = split(exp[0], done)
		exp[0] = lexp
		rexp, done = split(exp[1], done)
		exp[1] = rexp
		return exp, done
	
# returns ex, remains
def qexplode(exp):
	# print(f'in qexplode ... maxd: {max(ds(exp))}')
	exp, remains = get_explodee(exp)
	# print(f'after get_explodee with {exp} -- {remains}')
	apply_explodee(exp, remains)
	# print(f'after apply_explodee with {exp}')
	renumber(exp)
	# print(f'after renumber with {exp}')
	return exp, remains

def qsplit(exp):
	# print(f'in qsplit ... maxv: {[v for v in vs(exp) if v > 9]}')
	exp, splitted = split(exp)
	# print(f'after split with {exp}')
	renumber(exp)
	# print(f'after renumber with {exp}')
	return exp, splitted

# returns exp (but doesn't really have to?)
def reduce(exp):
	exploded = True
	
	# if you exploded once, try again:
	while exploded:
		exp, exploded = qexplode(exp)
		# if exploded: print(f'exploded to: {ts(exp)} w/ remains={exploded}')
		# if exploded: printy(exp,0,'exploded to')
		

	exp, splitted = qsplit(exp)

	if splitted:
		# print(f'splitted to: {ts(exp)}')
		# printy(exp,0,'splitted to')
		exp = reduce(exp)
	return exp

def qparse(exp):
	# exp always comes back in singular array
	_, exp = parse(exp)

	exp = exp[0]
	renumber(exp)
	return exp

# exploding tests
# explode_tests = [
# '[[[[[9,8],1],2],3],4]',
# '[7,[6,[5,[4,[3,2]]]]]',
# '[[6,[5,[4,[3,2]]]],1]',
# '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]',
# '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
# ]
# for exp in explode_tests:
# 	exp = qparse(exp)
# 	prints(exp)
# 	exp, _ = qexplode(exp)
# 	prints(exp)
# 	print('\n')

# reducing tests
# e1 = qparse('[[[[4,3],4],4],[7,[[8,4],9]]]')
# e2 = qparse('[1,1]')
# prints(e1)
# prints(e2)
# v = add(e1, e2)
# prints(v)
# v = reduce(v)
# prints(v)

# f = [x for x in open("testdunno.txt").read().strip().split('\n')]

# for exp in f:
# 	print(exp)
# 	exp = qparse(exp)
# 	print(f'{ts(exp)}')
# 	exp = reduce(exp)
# 	print(f'{ts(exp)}\n\n')

def ts(v):
	return ''.join([x for x in str(v) if x != ' '])

def prints(v):
	print(ts(v))

# depths
def printy(ex, d=0, prefix = ''):
	# if d == 0:
	# 	print(prefix, end='  ')

	c = 'white'
	if d > 4: c = 'red'

	if isinstance(ex, list):
		print(colored('[', c), end='')
		printy(ex[0], d+1)
		print(colored(',', c), end='')
		printy(ex[1], d+1)
		print(colored(']', c), end='')
	else:
		print(colored(ex, c), end='')

	if d==0:
		print()


f = [x for x in open("input.txt").read().strip().split('\n')]

v = None
for exp in f:
	exp = qparse(exp)

	if v == None:
		v = exp
	else:
		v = add(v, exp)
		v = reduce(v)
print('part1', magnitude(v))



L = len(f)
out = []
for i in range(L):
	for j in range(L):
		if i!=j:
			out.append(magnitude(reduce(add(qparse(f[i]), qparse(f[j])))))

print('part2', max(out))




