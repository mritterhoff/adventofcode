from pprint import pprint
import math
import numpy as np
f = [x for x in open("input.txt").read().strip().split('\n')]
f = np.asarray([[y for y in x] for x in f])


def out(fold, fnew, x, y):
	if fold[y][x] == '.':
		fnew[y][x] = '.'
		return

	xmax = len(fold[0])
	ymax = len(fold)
	x_range = range(max(x-1,0), min(x+2,xmax))
	y_range = range(max(y-1,0), min(y+2,ymax))
	count = 0
	for ix in x_range:
		for iy in y_range:
			if (iy,ix) != (y,x) and fold[iy][ix] == '#':
				count+=1

	if fold[y][x] == 'L' and count == 0:
		fnew[y][x] = '#'
	elif fold[y][x] == '#' and count >= 4:
		fnew[y][x] = 'L'
	else:
		fnew[y][x] = fold[y][x]

def times(m, pt):
	return (pt[0]*m, pt[1]*m)

def in_range(xmax, ymax, x, y):
	# TODO or is it max+1
	return x in range(0, xmax) and y in range(0, ymax)

def get_hash_count(f, x_o, y_o):
	xmax = len(f[0])
	ymax = len(f)

	ds = [(-1, -1), (-1, 0), (-1, 1), 
		( 0, -1), ( 0, 1),
		( 1, -1), ( 1, 0), ( 1, 1)]

	hash_count = 0
	for d in ds:
		# print(d)
		m = 1
		while True:
			d_mult = times(m, d)
			x = x_o + d_mult[0]
			y = y_o + d_mult[1]
			if in_range(xmax, ymax, x, y):
				# print(f[y][x])
				if f[y][x] == '.':
					# print('found .')
					pass
				elif f[y][x] == '#':
					# print('found #', d_mult)
					hash_count += 1
					break
				else:
					# print('found L', d_mult)
					break
			else:
				# print('hit wall', d_mult)
				break
			m+=1

	return hash_count



def out2(fold, fnew, x, y):
	# print(fold)
	if fold[y][x] == '.':
		# print('. duh')
		fnew[y][x] = '.'
		return

	count = get_hash_count(fold, x, y)

	if fold[y][x] == 'L' and count == 0:
		fnew[y][x] = '#'
	elif fold[y][x] == '#' and count >= 5:
		fnew[y][x] = 'L'
	else:
		fnew[y][x] = fold[y][x]

rez = [f]

for gen in range(1, 1000):
	fold = rez[-1]
	fnew = np.empty([len(fold[0]), len(fold)], dtype=str)
	for iy, row in enumerate(fold):
		for ix, el in enumerate(row):
			out2(fold,fnew,ix,iy)
	rez.append(fnew)
	if np.array_equal(rez[-1],rez[-2]):
		break

# for i, ar in enumerate(rez):
# 	print('gen', i,'\n', ar)

count = 0
for x in rez[-1]:
	for y in x:
		if y=='#':
			count+=1
print(count)