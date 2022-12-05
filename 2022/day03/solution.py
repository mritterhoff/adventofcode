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

f = [x for x in open("input.txt").read().strip().split('\n')]

def worth(p):
	if p.isupper():
		return ord(p) - ord('A') + 27
	else:
		return ord(p) - ord('a') + 1

score = 0
for rs in f:
	s = int(len(rs)/2)
	score += worth(list(set(rs[:s]).intersection(set(rs[s:])))[0])
print('p1:', score)


score = 0
for x in range(0, len(f), 3):
	s1,s2,s3 = set(f[x]), set(f[x+1]), set(f[x+2])
	score += worth(list(set(s1.intersection(s2).intersection(s3)))[0])
print('p2:', score)
