from parse import *

# DEBUG = True
DEBUG = False

def print1(*a):
	if DEBUG: print(*a)

def pad(total, num_str):
	rez = (total-len(num_str))*'0' + "".join(num_str)
	return rez

def apply_mask(mask, num):
	print1(mask, list(num))
	num = list(pad(len(mask), list(num)))
	print1("".join(num))
	for i in range(0, len(mask)):
		if mask[i] in ['0', '1']:
			num[i] = mask[i]
	print11("".join(num))
	return "".join(num)


def part1():
	mem = {}
	mask = ''
	for line in [x for x in open("input.txt").read().strip().split('\n')]:
		p1 = parse("mask = {}", line)
		p2 = parse("mem[{}] = {}", line)
		if p1:
			# print1(p1[0])
			mask = p1[0]
		elif p2:
			# print1(p2[0], p2[1])
			mem[p2[0]] = apply_mask(mask, bin(int(p2[1]))[2:])

	print1(mem)

	print1([int(x, 2) for x in mem.values()])

	print1(sum([int(x, 2) for x in mem.values()]))

def part2():
	mem = {}
	mask = ''
	for line in [x for x in open("input.txt").read().strip().split('\n')]:
		p1 = parse("mask = {}", line)
		p2 = parse("mem[{}] = {}", line)
		if p1:
			mask = p1[0]
		elif p2:
			address = bin(int(p2[0]))[2:]
			val_to_set = int(p2[1])

			local_mask = address_mask_combine(address, mask)
			print1('local_mask', local_mask)
			addys = addresses_from_masks(local_mask)
			print1('address', address, 'mask', mask, 'local_mask', local_mask, 'addys count', len(addys))
			for x in addys:
				mem[x] = val_to_set


	print(len(mem), 'entries')
	print(sum([x for x in mem.values()]))

def replace(mask, bools):
	m_arr = list(mask)
	x_c = 0
	for i, c in enumerate(m_arr):
		if c == 'X':
			m_arr[i] = bools[x_c]
			x_c += 1
	return "".join(m_arr)

def address_mask_combine(address, mask):
	address = pad(len(mask), address)
	rez = []
	for i, c in enumerate(list(mask)):
		if mask[i] == '0':
			rez.append(address[i])
		elif mask[i] == '1':
			rez.append(mask[i])
		else:
			rez.append('X')
	return "".join(rez)




# given a mask w/ Xs, we need to generate every substitution of 0/1 for X's
# make it return an array of ints
def addresses_from_masks(mask):
	rez = []
	xcount = len([x for x in list(mask) if x == 'X'])
	print1('xcount', xcount)
	for i in range(0,2**xcount):
		b = pad(xcount,bin(int(i))[2:])
		rez.append(replace(mask, list(b)))
	return rez



part2()









