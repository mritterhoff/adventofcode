f = open("input.txt").read().strip()

def solve(offset):
	for i in range(0, len(f) - offset):
		if len(set(f[i:i+offset])) == offset:
			return i + offset

print('p1:', solve(4))
print('p2:', solve(14))