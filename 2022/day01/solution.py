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


# attempt 1
f = [x for x in open("input.txt").read().strip().split('\n')]
list = []
local = []
for x in f:
	if x == '':
		list.append(sum(local))
		local = []
	else:
		local.append(int(x))
list.sort()
print('part 1 solution:',list[-1])
print('part 2 solution:',sum(list[-3:]))


# attempt 2
f = [y.split('\n') for y in open("input.txt").read().strip().split('\n\n')]
sums = sorted([sum([int(y) for y in x]) for x in f])
print('part 1 solution:',sums[-1])
print('part 2 solution:',sum(sums[-3:]))