import pprint
import heapq as hq
import functools, operator
from functools import cache
from termcolor import colored
import itertools

import math
import numpy as np
import copy
from collections import defaultdict, Counter
from parse import *

f = [int(x) for x in open("input.txt").read().strip().split(',')]
og = f.copy()

i = 0
dic = {}
for ff in f:
	dic[i] = ff
	i = i + 1

def get_input():
	return 1

def get(dic, value, param):
	if param == '0':
		return dic[value]
	else:
		return value

def run(dic, p):

	insky = str(dic[p])
	# print('running with:', p, insky)

	opcode = int(insky[-2:])
	params = insky[:-2].zfill(5)[::-1]

	if opcode == 1:
		t1 = get(dic, dic[p+1], params[0])
		t2 = get(dic, dic[p+2], params[1])
		dic[dic[p+3]] = t1 + t2

		run(dic, p+4)
	elif opcode == 2:
		t1 = get(dic, dic[p+1], params[0])
		t2 = get(dic, dic[p+2], params[1])
		dic[dic[p+3]] = t1 * t2

		run(dic, p+4)
	elif opcode == 3:
		dic[dic[p+1]] = get_input()
		run(dic, p+2)

	elif opcode == 4:
		t1 = get(dic, dic[p+1], params[0])
		print("output!!!", t1)
		run(dic, p+2)
		
	elif opcode == 99:
		return
	else:
		print('opcode is bad:', opcode)

## part 1 
run(dic, 0)
print('p1 solution:', dic[0])

# # part 2
# for n,v in itertools.product(range(100), range(100)):
# 	dic = og.copy()
# 	dic[1] = n
# 	dic[2] = v
# 	run(dic, 0)
# 	if dic[0] == 19690720:
# 		print('p2 solution:', n*100 + v)
# 		break


