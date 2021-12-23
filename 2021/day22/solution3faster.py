import pprint
import functools, operator
from functools import cache
import itertools
from collections import defaultdict, Counter

import math


debug = False

def tupify(x):
	return x if type(x) is tuple else tuple(x)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# arr = [(1,2), (3,4), (5,6)]

# for a in chunks(arr, 2):
# 	print(a)


# assert False


@cache
def engulf(r1, r2):
	r1s, r1e = r1
	r2s, r2e = r2
	justr2 = []
	# figure out what the parts that are only r2 are
	if r1s == r2s:
		#begnnings are the same
		justr2 = [(r1e+1, r2e)]
	elif r1e == r2e:
		# ends are the same
		justr2 = [(r2s, r1s-1)]
	else:
		# it's a bit easier
		justr2 = [(r2s, r1s-1), (r1e+1, r2e)]
	return tuple([(), tuple([tuple(r1)]), tuple(justr2)])

@cache
def partial(r1, r2):
	r1s, r1e = r1
	r2s, r2e = r2
	return tuple([tuple([(r1s, r2s-1)]), tuple([(r2s, r1e)]), tuple([(r1e+1, r2e)])])

def combineifposs(pair):
	a, b = pair
	# there can only be one pair of cords that aren't the same,
	# and they have to be one off on one side
	if a[0:4] == b[0:4]:
		az, azz = a[4:]
		bz, bzz = b[4:]
		if azz + 1 == bz or bzz + 1 == az:
			return [tuple([*a[0:4], min(*a[4:], *b[4:]), max(*a[4:], *b[4:]) ])]
	elif a[0:2] == b[0:2] and a[4:] == b[4:]:
		ay, ayy = a[2:4]
		by, byy = b[2:4]
		if ayy + 1 == by or byy + 1 == ay:
			return [tuple([*a[0:2], min(*a[2:4], *b[2:4]), max(*a[2:4], *b[2:4]), *a[4:] ])]

	elif a[2:] == b[2:]:
		ax, ax = a[0:2]
		bx, bx = b[0:2]
		if ax + 1 == bx or bx + 1 == ax:
			return [tuple([min(*a[0:2], *b[0:2]), max(*a[0:2], *b[0:2]), *a[2:] ])]
	return pair


# these are both len 2 lists
@cache
def compare(r1s, r1e, r2s, r2e):
	# print(f'compare {r1}, {r2}')

	r1r = range(r1s, r1e+1)
	r2r = range(r2s, r2e+1)

	if r1r == r2r:
		if debug: print(f'r1 {(r1s, r1e)} is the same as {(r2s, r2e)}')
		return tuple([(), ((r1s, r1e)), ()])

	if r1s in r2r and r1e in r2r:
		if debug: print(f'r1 {(r1s, r1e)} completely in r2 {(r2s, r2e)}')
		return engulf((r1s, r1e), (r2s, r2e))

	if r2s in r1r and r2e in r1r:
		if debug: print(f'r1 {(r1s, r1e)} completely around r2 {(r2s, r2e)}')
		return tuple(reversed(engulf((r2s, r2e), (r1s, r1e))))

	# from here on, it's partial or not at all
	if r1e in r2r and r2s in r1r:
		if debug: print(f'r1 {(r1s, r1e)} partially overlaps with r2 {(r2s, r2e)} way 1')
		return partial((r1s, r1e), (r2s, r2e))
	if r1s in r2r and r2e in r1r:
		if debug: print(f'r1 {(r1s, r1e)} partially overlaps with r2 {(r2s, r2e)} way 2')
		return tuple(reversed(partial((r2s, r2e), (r1s, r1e))))


	if debug: print(f'r1 {(r1s, r1e)} does not overlap with r2 {(r2s, r2e)}')
	return tuple([tuple([(r1s, r1e)]), (), tuple([(r2s, r2e)])])



f = [x for x in open("input.txt").read().strip().split('\n')]


def size(x, xx, y, yy, z, zz):
	return (xx-x+1)*(yy-y+1)*(zz-z+1)


dirs = []
for l in f:
	state, rest = l.split(' ')
	dimens = rest.split(',')
	outline = [state]
	for d in dimens:
		a = d[0] # xyz
		limits = d[2:].split('..')
		limits = [int(x) for x in limits]
		outline.extend(limits)
	dirs.append(outline)


# initially, 70 took real    0m6.500s

cubes = set()
L = len(dirs)
i = 0
for newcube in dirs:
	sizes = defaultdict(int)
	print(f'on {i} out of {L}')
	i += 1
	cubes2 = set()

	turnon = newcube[0] == 'on'

	# add our new tcube first, check if subsequent cubes overlap,
	# and only add the non-overlapping bits. they won't overlap with each other
	if turnon: cubes2.add(tuple(newcube[1:]))

	for existingcube in cubes:
		xover = compare(*existingcube[0:2], *newcube[1:3])
		yover = compare(*existingcube[2:4], *newcube[3:5])
		zover = compare(*existingcube[4:], *newcube[5:])
		# print(xover)
		# print(yover)
		# print(zover)


		# TODO is this sufficient? can we more quickly figure out if there definitely isn't overlap?

		noEConly = all(EConly==() for (EConly,_, _) in [xover, yover, zover])
		if noEConly:
			pass
			# print(f'there are no overlaps!') # for the combo {existingcube} and {newcube}')
			# cubes2.add(existingcube)
		else:
			# the 1st and 3rd term of each dimen overlap array COULD be
			# a list of 2 tuples, rather than just a tuple

			# we only need to add the leftmost/middle laps, which belong to existing cube
			# because we added the newcube
			cubestoadd = []
			for ix in range(0,2):
				for iy in range(0,2):
					for iz in range(0,2):
						if ix == iy == iz == 1:
							#this would mean that we're not looking at ANY leftmost only parts
							continue
						for c in itertools.product(xover[ix],yover[iy],zover[iz]):
							x,y,z = c
							# print('xyz is', x, y, z)
							# print('adding', adding)
							cubestoadd.append(tuple([*x, *y, *z]))
							# sizes[size(*x, *y, *z)] += 1
			for chunk in chunks(cubestoadd, 2):
				if len(chunk) == 2:
					# pass
					chunk = combineifposs(chunk)
				cubes2.update(chunk)
			

	# for k in sorted(sizes.keys())[0:100]:
	# 	print(f'{k}-sized cuboids exist {sizes[k]} times')

	# print(f'there are {len(cubes2)} in cubes2')
	cubes = cubes2






print('done!')

total = 0
for c in cubes:
	total += size(*c)

print(total)
# assert 2758514936282235 == total

# TODO this is where we tally up cubes