import pp
import heapq as hq
import functools, operator
from functools import cache
from termcolor import colored

import math
import string
import numpy as np
import copy
from collections import defaultdict, Counter
from parse import *

f = [x for x in open("input.txt").read().strip().split('\n')]

# f = "dabAcCaCBAcCcaDA"

@cache
def cancel(x, y):
	if x.lower() != y.lower():
		return False
	if (x.isupper() and y.islower()) or (x.islower() and y.isupper()):
		return True
	return False;

def reduce(f, x = None):
	hist = ["", ""]
	ignore = []
	if x:
		ignore = [x, x.upper()]
	while f != hist[-2]:
		fp = []
		idx = 0
		while idx < len(f):
			if x and f[idx] in ignore:
				idx += 1
				continue
			if idx == len(f) - 1:
				fp.append(f[idx])
				break
			if cancel(f[idx], f[idx+1]):
				idx += 2
			else:
				fp.append(f[idx])
				idx += 1

		f = "".join(fp)
		hist.append(f)
		# print(f)

	return len(hist[-1])

print('p1', reduce(f))

mm = 10000000000
for x in list(string.ascii_lowercase):
	mm = min(mm, reduce(f, x))
	print(x, mm)
print(mm)









