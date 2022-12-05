f = [int(x) for x in open("input.txt").read().strip().split('\n')]

print('p1:', sum(f))

def func(past, freq):
	for x in f:
		freq += x
		if freq in past:
			return freq
		past.add(freq)
	return func(past, freq)

print('p2:', func(set([0]), 0))