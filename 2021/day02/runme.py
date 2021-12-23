# https://adventofcode.com/2021/day/2


def part_1():
	file1 = open("input.txt")

	# part 1
	x = 0
	y = 0

	funcs = {
		"forward": lambda x, y, z: [x+z, y],
		"up": lambda x, y, z: [x, y-z],
		"down": lambda x, y, z: [x, y+z]
	}

	for line in file1:
		print(line)
		split = line.split(" ")
		print("old: {} , {}".format(x, y))
		rez = funcs[split[0]](x, y, int(split[1]))
		x = rez[0]
		y = rez[1]
		print("new: {} , {}".format(x, y))

	print(x*y)

def part_2():
	file1 = open("input.txt")

	# part 1
	x = 0
	y = 0
	aim = 0

	funcs = {
		"forward": lambda x, y, aim, z: [x+z, y + aim*z, aim],
		"up": lambda x, y, aim, z: [x, y, aim - z],
		"down": lambda x, y, aim, z: [x, y, aim + z]
	}

	for line in file1:
		print(line)
		split = line.split(" ")
		print("old: x:{} y:{} aim:{}".format(x, y, aim))
		rez = funcs[split[0]](x, y, aim, int(split[1]))
		x = rez[0]
		y = rez[1]
		aim = rez[2]
		print("new: x:{} y:{} aim:{}".format(x, y, aim))

	print(x*y)


part_2()