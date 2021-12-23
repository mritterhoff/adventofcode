from collections import Counter
from functools import cache

f = sorted([int(x) for x in open("input.txt").read().strip().split('\n')])

def part1():
	print(f)

	f.insert(0, 0)
	f.append(f[-1] + 3)

	zipped = list(zip(f[1:],f[:-1]))

	cnt = Counter([x-y for x,y in zipped])

	print(cnt[1]*cnt[3])


f.insert(0, 0)
f.append(f[-1] + 3)
print(f)

@cache
def did_get_to_end(x):
	curr_index = f.index(x)
	if curr_index == len(f) - 1 :
		return 1

	l = curr_index+1
	r = min(curr_index+4,len(f))
	return sum([did_get_to_end(x) for x in f[l:r] if x-f[curr_index] <= 3])

def did_get_to_end_2(dict,x):
	if x in dict.keys():
		return dict[x]

	curr_index = f.index(x)
	if curr_index == len(f) - 1 :
		dict[x] = 1
		return 1

	l = curr_index+1
	r = min(curr_index+4,len(f))
	val = sum([did_get_to_end_2(dict,x) for x in f[l:r] if x-f[curr_index] <= 3])
	dict[x] = val
	return val

print(did_get_to_end(0))
print(did_get_to_end_2({}, 0))