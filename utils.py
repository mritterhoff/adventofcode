import math
import copy
import string
import pp
import heapq as hq
import functools, operator
from functools import cache, reduce
from termcolor import colored
import itertools as it
import numpy as np
from collections import defaultdict, Counter, deque
from parse import *

inf = float("inf")


# Return 2-d neighbors of point (as pair) with bounds.
# p, C, R = (1,1), 5, 5 
# print(ns((1,1), R, C))
def ns_4(p, R, C):
	x,y = p
	dirs = [(1,0), (-1,0), (0,1), (0,-1)]  # right/left/up/down
	return [(x+dx, y+dy) for dx,dy in dirs if 0<= x+dx < C and 0<= y+dy < R]

def ns_8(p, R, C):
	x,y = p
	dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)] # all 8 neighbors
	return [(x+dx, y+dy) for dx,dy in dirs if 0<= x+dx < C and 0<= y+dy < R]