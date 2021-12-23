f = [x for x in open("input.txt").read().strip().split('\n')]

def binsearch(s, go_l, l, r):
	for c in s:
		if c == go_l:
			r = r - (r-l)//2 - 1
		else:
			l = l + (r-l)//2 + 1
		# print(c, l, r)
	return l

def id(s):
	row = binsearch(s[:7], 'F', 0, 127)
	col = binsearch(s[-3:], 'L', 0, 7)
	return row*8 + col

print('part 1:', max([id(x) for x in f]))
o = sorted([id(x) for x in f])
print('part 2:', [x for x in range(o[0], o[-1] + 1) if x not in o][0])