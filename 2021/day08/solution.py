import math

f = [x for x in open("input.txt").read().strip().split('\n')]
f = [x.split(' | ') for x in f]

# part 1
count = 0
for p in f:
	seg = p[1].split(' ')
	for x in seg:
		#            d1  d7 d4 d8
		if len(x) in [2, 3, 4, 7]:
			count += 1

print('part1:', count)


def get_letters_from_value(dict, v_in):
	return next(key for key, value in dict.items() if value == v_in)


# digit d1 d2 d3 d4 d5 d6 d7 d8 d9 d0
# count  2  5  5  4  5  6  3  7  6  6

# 5seg -> d2, d3, d5
# 6seg -> d6, d9, d0

#  read left side of |
#  generate a mapping of sorted string to number
#  use look up the 4 sorted values in the 2nd part
def generate_map(left):
	m = {}
	lefts = left.split(' ')
	g = ["".join(sorted(x)) for x in lefts]

	# d1  d7 d4 d8
	# [2, 3, 4, 7]
	for x in g:
		if len(x) == 2:
			m[x] = 1
		elif len(x) == 3:
			m[x] = 7
		elif len(x) == 4:
			m[x] = 4
		elif len(x) == 7:
			m[x] = 8

	for x in g:
		if len(x) == 6:
			# 9 has all the chars 4 has, 6, 0 don't
			# 0 has all the chars 1 has, 6 doesn't
			# else 6
			letters4 = get_letters_from_value(m, 4)
			letters1 = get_letters_from_value(m, 1)

			if set([y for y in x]).issuperset(set([z for z in letters4])):
				m[x] = 9
			elif set([y for y in x]).issuperset(set([z for z in letters1])):
				m[x] = 0
			else:
				m[x] = 6

	for x in g:
		if len(x) == 5:
			# 3 has all the chars 1 has (2 and 5 don't)
			# 5 has all the same chars as 6 exept 1
			# else 2
			
			letters6 = get_letters_from_value(m, 6)
			letters1 = get_letters_from_value(m, 1)

			if set([y for y in x]).issuperset(set([z for z in letters1])):
				m[x] = 3
			elif set([z for z in letters6]).issuperset(set([y for y in x])):
				m[x] = 5
			else:
				m[x] = 2

	return m

counter = 0
for p in f:
	m = generate_map(p[0])

	rez = ''
	for x in p[1].split(' '):
		srted = "".join(sorted(x))
		rez += str(m[srted])
	counter += int(rez)

print('part2:', counter)

