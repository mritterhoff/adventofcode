import sys 
sys.path.append('../..')
from utils import *
from functools import cmp_to_key

f = [x for x in open("input.txt").read().strip().split('\n\n')]

pairs = [x.split('\n') for x in f]

allVals = []
for p in pairs:
	allVals.append(p[0])
	allVals.append(p[1])


allVals.append('[[2]]')
allVals.append('[[6]]')

count = 0


def compare(left, right):
	global count

	ltype, rtype = type(left), type(right)

	try:
		if ltype == int and rtype == int:
			if left > right:
				return False
			if left < right:
				return True
			return None
		if ltype == list and rtype == list:
			for i in range(len(left)):
				rez = compare(left[i], right[i])
				if rez != None: return rez
			if range(len(left)) == range(len(right)):
				return None
			else:
				return True
			
		if ltype == list and rtype == int:
			rez = compare(left, [right])
			if rez != None: return rez
		if ltype == int and rtype == list:
			rez = compare([left], right)
			if rez != None: return rez
		return True
	except Exception as inst:
		if len(left) < len(right):
			return True
		else:
			return False


# for idx, pair in enumerate(pairs):
# 	idx = idx + 1
# 	# if idx == 2:
# 	left = pair[0]
# 	right = pair[1]
# 	if compare(eval(left), eval(right)):
# 		count += idx
# 		print('good', idx, left, right)

def meth(a, b):
	rez = compare(eval(a), eval(b))
	return -1 if rez else 1


allVals = sorted(allVals, key=cmp_to_key(meth))

pp(allVals)

i1 = allVals.index('[[2]]') + 1
i2 = allVals.index('[[6]]') + 1
print(i1 * i2)























