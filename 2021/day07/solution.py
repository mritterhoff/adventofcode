import math

f = [int(x) for x in open("input.txt").read().strip().split(",")]

def part1():
	sums = []
	for x in range(min(f), max(f)+1):
		sum = 0 
		for fin in f: sum+= abs(x-fin)
		sums.append(sum)
	print(min(sums))


def part2():
	sums = []
	for x in range(min(f), max(f)+1):
		sum = 0 
		for fin in f:
			diff = abs(x-fin) 
			new_sum =0
			if diff == 0:
				new_sum = diff
			else:
				new_sum = (diff + 1)*diff/2
			sum += new_sum
		sums.append(sum)
	print(min(sums))

part1()
part2()