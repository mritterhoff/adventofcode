import math
f = [int(x) for x in open("input.txt").read().strip().split('\n')]

preamble = 25

def sum_of_two_prev(f,pos,preamble,matchme):
	for ind, x in enumerate(f[pos-preamble:pos]):
		for ind2, x2 in enumerate(f[pos-preamble:pos]):
			if ind != ind2 and x + x2 == matchme:
				return True
	return False


for ind, x in enumerate(f):
	if ind >= preamble:
		if sum_of_two_prev(f, ind, preamble, x):
			pass
		else:
			part1_ans = x 
			break

print(part1_ans)

def part2(findme):
	for i, x in enumerate(f):
		for j, x in enumerate(f):
			intv = f[i:j+1]
			if sum(intv) == part1_ans:
				return min(intv) + max(intv)

print(part2(part1_ans))