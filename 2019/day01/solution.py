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


# part 1
f = [x for x in open("input.txt").read().strip().split('\n')]

fules = [math.trunc(int(x)/3.0)-2 for x in f]

print(sum(fules))


# part 2

def calc(a):
	out = math.trunc(int(a)/3.0)-2
	if out > 0:
		return out
	else:
		return 0

total = 0
for fule in fules:
	while fule > 0:
		total = total + fule
		fule = calc(fule)

print(total)

