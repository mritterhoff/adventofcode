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


poss = []
for num in range(172851, 675869+1):
	last_i = -1
	min = -1
	dubs = False
	for i in [int(x) for x in str(num)]:
		if not dubs:
			dubs = i == last_i
			last_i = i
		if i < min:
			min = 100
			break
		min = max(i, min)
	if min < 100 and dubs:
		poss.append(num)
print("part 1:", len(poss))


def reps(num):
	rez = []
	hist = []
	for x in [int(x) for x in str(num)]:
		if len(hist) == 0:
			hist.append(x)
		else:
			if hist[-1] == x:
				hist.append(x)
			else:
				if len(hist) > 1:
					rez.append(len(hist))
				hist = []
				hist.append(x)
	if len(hist) > 1:
		rez.append(len(hist))
	return rez

count = 0
for num in poss:
	if 2 in reps(num):
		count += 1
print("part 2:", count)








