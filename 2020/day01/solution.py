# find the two entries that add to 2020 and then multiply them together

f = [int(x) for x in open("input.txt").read().strip().split('\n')]
print(f)

def part_1():
	o = [2020 - x for x in f]

	for s in o:
		if s in f:
			print(s, 2020-s, (2020-s)*s)
			break


# part 2

def part_2():
	for x in f:
		for y in f:
			for z in f:
				if x+y+z == 2020:
					print(x, y, z, x*y*z)
					return

part_2()