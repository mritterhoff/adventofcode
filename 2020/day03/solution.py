import math

f = [x for x in open("input.txt").read().strip().split('\n')]

counts = []
for tx,ty in [(3,1),(1,1),(5,1),(7,1),(1,2)]:
	x = y = count = 0
	while y < len(f):
		if f[y][x] == '#':
			count += 1
		y += ty
		x = (x + tx) % len(f[0])
	counts.append(count)

print (counts, math.prod(counts))