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

def run(dic, p):
	opcode = dic[p]
	if opcode == 1:
		dic[dic[p+3]] = dic[dic[p+1]] + dic[dic[p+2]]
		run(dic, p+4)
	elif opcode == 2:
		dic[dic[p+3]] = dic[dic[p+1]] * dic[dic[p+2]]
		run(dic, p+4)
	elif opcode == 99:
		return
	else:
		print(['opcode is bad:',opcode].join())

## part 1 
dic[1] = 12
dic[2] = 2
run(dic, 0)
print('p1 solution:', dic[0])

# part 2
for n,v in itertools.product(range(100), range(100)):
	dic = og.copy()
	dic[1] = n
	dic[2] = v
	run(dic, 0)
	if dic[0] == 19690720:
		print('p2 solution:', n*100 + v)
		break







