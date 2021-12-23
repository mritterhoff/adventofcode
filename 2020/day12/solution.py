import math

f = [x for x in open("input.txt").read().strip().split('\n')]


def part_1():
	deg = 0 # east
	x = 0
	y = 0

	for instr in f:
		ch = instr[0]
		num = int(instr[1:])

		if ch == 'N':
			y += num
		elif ch == 'S':
			y -= num
		elif ch == 'E':
			x += num
		elif ch == 'W':
			x -= num
		elif ch == 'L':
			deg += num
		elif ch == 'R':
			deg -= num
		elif ch == 'F':
			x += num*math.cos(math.radians(deg))
			y += num*math.sin(math.radians(deg))

	print('part1:', round(abs(x)+abs(y)))

def part_2():
	x = 0
	y = 0
	x_w = 10
	y_w = 1

	for instr in f:
		ch = instr[0]
		num = int(instr[1:])

		if ch == 'N':
			y_w += num
		elif ch == 'S':
			y_w -= num
		elif ch == 'E':
			x_w += num
		elif ch == 'W':
			x_w -= num
		elif ch in ['L', 'R']:
			if ch == 'R':
				num = 360 - num
			if num == 90:
				#3, 1 -> -1, 3
				x_w_t = x_w
				y_w_t = y_w
				x_w = -y_w_t
				y_w =  x_w_t
			elif num == 180:
				#3, 1 -> -3, -1
				x_w_t = x_w
				y_w_t = y_w
				x_w = -x_w_t
				y_w = -y_w_t
			elif num == 270:
				#-1, 3 -> 3, 1
				x_w_t = x_w
				y_w_t = y_w
				x_w = y_w_t
				y_w = -x_w_t
			else:
				raise "i'm sad now"
		elif ch == 'F':
			x += num*x_w
			y += num*y_w

	print('part2:', abs(x)+abs(y))

part_1()
part_2()