# don't strip the last empty line(s)
f = [x for x in open("input.txt").read().split('\n')]

def runme(part_2=False):
	count = 0
	d = {}
	people_count = 0
	for l in f:
		if len(l) == 0:
			if part_2:
				count += sum([x==people_count for x in d.values()])
			else:
				count += len(d.keys())
			d = {}
			people_count = 0
		else:
			for c in l:
				d[c] = d.get(c, 0) + 1
			people_count += 1
	print(count)

runme()
runme(True)
