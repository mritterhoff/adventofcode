import sys 
sys.path.append('../..')
from utils import *

f = [x for x in open("input.txt").read().strip().split('\n\n')]

pairs = [x.split('\n') for x in f]

pp(pairs)


count = 0



def compare(left, right):
	global count

	ltype, rtype = type(left), type(right)



	print('comparing', left, right)
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




for idx, pair in enumerate(pairs):
	idx = idx + 1
	# if idx == 2:
	left = pair[0]
	right = pair[1]
	if compare(eval(left), eval(right)):
		count += idx
		print('good', idx, left, right)



print(count)


# not 6104,5893
































