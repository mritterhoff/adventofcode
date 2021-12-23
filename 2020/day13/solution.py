# https://adventofcode.com/2020/day/13

import math
import numpy as np

f = [x for x in open("input.txt").read().strip().split('\n')]

def part1():
	time = int(f[0])
	busses = [int(x) for x in f[1].split(',') if x != 'x']

	print (time, busses)

	pairs = []
	for x in busses:
		d = time // x
		t = (d + 1)*x
		id = x
		wait = t - time
		pairs.append((wait, id))

	min_pair = min(pairs, key = lambda p: p[0])
	print(pairs)
	print(min_pair)
	print(min_pair[0]*min_pair[1])

def part2():
	i = [x for x in f[1].split(',')]

	id_offsets = []
	for ind, x in enumerate(i):
		if x != 'x':
			id_offsets.append({'bus':int(x), 'index':ind})

	id_offsets = sorted(id_offsets, key=lambda p: p['index'])
	print(id_offsets)

	# inc by 7 until 2nd one is right, then mult by their product until next one is right
	t = id_offsets[0]['bus']
	for i,e in enumerate(id_offsets):
		if i == 0: continue

		inc = np.prod([x['bus'] for x in id_offsets[0:i]])
		this_index = id_offsets[i]['index']
		this_bus = id_offsets[i]['bus']

		while (t+this_index)%this_bus !=0:
			t += inc
		print('new t:', [(t+x['index']) for x in id_offsets[0:i]])

		print(t)

part2()	

842,186,186,521,918

# # 0  1 2 3  4 5  6  7
#   7,13,x,x,59,x,31,19


#   time    				 bus 7   bus 13  bus 59  bus 31  bus 19
# 1068773   				 .       .       .       .       .
# 1068774   				 D       .       .       .       .
# 1068775   				 .       .       .       .       .
# 1068776   				 .       .       .       .       .
# 1068777   				 .       .       .       .       .
# 1068778   				 .       .       .       .       .
# 1068779   				 .       .       .       .       .
# 1068780   				 .       .       .       .       .
# 1068781 = 7*152683		 D       .       .       .       .
# 1068782 = 13*82214		 .       D       .       .       .
# 1068783   				 .       .       .       .       .
# 1068784   				 .       .       .       .       .
# 1068785   				 .       .       D       .       .
# 1068786   				 .       .       .       .       .
# 1068787   				 .       .       .       D       .
# 1068788   				 D       .       .       .       D
# 1068789   				 .       .       .       .       .

# 1054113


# 3162341 = LCM (product of primes here)
# is the max right? because then they would all align again.

# can I get a direction to explore in?

# # bunch of equations?
# a * 7 = t1
# b * 13 = t1 + 1
# c * 59 = t1 + 4
# d * 31 = t1 + 6
# e * 19 = t1 + 7

# a * 7     = t1
# b * 13 -1 = t1
# c * 59 -4 = t1
# d * 31 -6 = t1
# e * 19 -7 = t1

# a         = t1 / 7
# b         = (t1 + 1)/13

# c * 59 -4 = t1

# d * 31 -6 = t1
# e * 19 -7 = t1

# 6 unknowns, 5 equations
