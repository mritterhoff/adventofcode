f = [x for x in open("input.txt").read().strip().split('\n')]

print(f)

m = {
	'}': '{',
	')': '(',
	'>': '<',
	']': '['
}

m_inv = {
	'{' : '}',
	'(': ')',
	'<': '>',
	'[': ']'
}

def is_valid(line):
	arr = []
	for c in line:
		if c in m.values():
			arr.append(c)
		elif c in m.keys():
			popped = arr.pop()
			if popped != m[c]:
				return c

	rez = []
	while len(arr) > 0:
		c = arr.pop()
		rez.append(m_inv[c])
	return rez

# rezes = []
# for line in f:
# 	rez = is_shitty(line)
# 	if rez != -1
# 		rezes.append(rez)

# score = 0
# for r in rezes:
# 	if r == ')':
# 		score += 3
# 	elif r == ']':
# 		score += 57
# 	elif r == '}':
# 		score += 1197
# 	elif r == '>':
# 		score += 25137
# 	else:
# 		raise "oh no"


def is_shitty(line):
	arr = []
	for c in line:
		if c in m.values():
			arr.append(c)
		elif c in m.keys():
			popped = arr.pop()
			if popped != m[c]:
				return -1

	# do real work here



rezes = []
for line in f:
	rez = is_valid(line)
	if len(rez) > 1:
		rezes.append(rez)

print('listen up!')
for r in rezes:
	print("".join(r))

scores = []
for row in rezes:
	score = 0
	for r in row:
		score = score * 5
		if r == ')':
			score += 1
		elif r == ']':
			score += 2
		elif r == '}':
			score += 3
		elif r == '>':
			score += 4
		else:
			print('uh ohhh', r)
			raise "oh no"
	scores.append(score)

print(scores)

scores = sorted(scores)
print(scores)

l = len(scores)
print(scores[int(l/2)])
