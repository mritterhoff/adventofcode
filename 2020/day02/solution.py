f = [x.split(':') for x in open("input.txt").read().strip().split('\n')]
f = [(*x.split(' '), y.strip()) for x,y in f]

def part_1():
	count = 0
	for con, ch, st in f:
		# print([int(x) for x in con.split('-')], ch, st)
		conl, conh = [int(x) for x in con.split('-')]

		cnt = len([x for x in st if x == ch])
		if cnt in range(conl, conh+1):
			count += 1

	print(count)

count = 0
for con, ch, st in f:
	print([int(x) for x in con.split('-')], ch, st)
	conl, conh = [int(x) for x in con.split('-')]

	if sum([st[conl-1] == ch, st[conh-1] == ch]) == 1:
		count +=1
print(count)