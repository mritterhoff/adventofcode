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

f = [x for x in open("input.txt").read().strip().split('\n')]
l1 = [(c[0], int(c[1:])) for c in f[0].split(',')]
l2 = [(c[0], int(c[1:])) for c in f[1].split(',')]


class Line:
    def __init__(self, start, end, ori, dir):
        self.start = start
        self.end = end
        self.ori = ori
        self.dir = dir

def trace(start, dirs):
	lines = []
	for dir, dist in dirs:
		match dir:
			case 'R':
				end = (start[0] + dist, start[1])
				lines.append(Line(start, end, "H", "R"))
			case 'L':
				end = (start[0] - dist, start[1])
				lines.append(Line(start, end, "H", "L"))
			case 'U':
				end = (start[0], start[1] + dist)
				lines.append(Line(start, end, "V", "U"))
			case 'D':
				end = (start[0], start[1] - dist)
				lines.append(Line(start, end, "V", "D"))
		start = end
	return lines


def between(v1, v2, c):
	return (v1 <= c <= v2) or (v1 >= c >= v2)

def intersections(l1_lines, l2_lines):
	xs = []
	for l1 in l1_lines:
		for l2 in l2_lines:
			if l1.ori == l2.ori:
				next
			v = l1 if l1.ori == "V" else l2
			h = l1 if l1.ori == "H" else l2
			if between(v.start[1], v.end[1], h.start[1]) and between(h.start[0], h.end[0], v.start[0]):
				xs.append((v.start[0], h.start[1]))
				# print('yay', (v[0][0], h[0][1]))
	return xs

l1_lines = trace((0, 0), l1)
l2_lines = trace((0, 0), l2)

xs = intersections(l1_lines, l2_lines)

dists = [abs(x[0]) + abs(x[1]) for x in xs]
print("p1 solution:", sorted(dists)[0] if sorted(dists)[0] != 0 else sorted(dists)[1])


def is_point_on_line(pt, line):
	if line.ori == 'V':
		# must be same x, and in between ys
		return line.start[0] == pt[0] and between(line.start[1], line.end[1], pt[1])
	else:
		# must be in between xs, and same ys
		return between(line.start[0], line.end[0], pt[0]) and line.start[1] == pt[1]

def partial_distance(pt, line):
	if line.ori == 'V':
		return abs(pt[1] - line.start[1])
	else:
		return abs(pt[0] - line.start[0])

def full_distance(line):
	if line.ori == 'V':
		return abs(line.end[1] - line.start[1])
	else:
		return abs(line.end[0] - line.start[0])\


# walk through each line in order. keeping track of distance.
# when you get to an intersection, add that partial distance and prev distance to mapped point. continue
# run through mapped values, fine smallest and corresponding point

def walk_the_line(d, xs, lines):
	clicks = 0
	for line in lines:
		for pt in xs:
			if is_point_on_line(pt, line):
				d[pt] += clicks + partial_distance(pt, line)
		clicks += full_distance(line)


d = defaultdict(int)
walk_the_line(d, xs, l1_lines)
walk_the_line(d, xs, l2_lines)

d = sorted(d.items(), key=lambda item: item[1])
print("p1 solution:", d[0][1] if d[0][1] != 0 else d[1][1])











