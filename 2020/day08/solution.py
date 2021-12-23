f = [x.split(' ') for x in open("input.txt").read().strip().split('\n')]
f = [(x,int(y)) for x,y in f]

def part_1():
	visted = set()
	acc = 0
	cursor = 0
	while cursor not in visted:
		visted.add(cursor)
		inst, arg = f[cursor]
		print(cursor, inst, arg)
		if inst == 'nop':
			cursor += 1
		elif inst == 'acc':
			acc += arg
			cursor += 1
		elif inst == 'jmp':
			cursor += arg
		else:
			raise 'oh no!'
	print(acc)


def part_2():

	# def flip_me(ind_to_flip, cursor):
	# 	my_ind = len([x for ind, x in enumerate(f) if x in ['jmp', 'nop'] and ind <= my_index])
	# 	return my_ind == ind_to_flip

	def try_it(a_f):
		visted = set()
		acc = 0
		cursor = 0
		while cursor not in visted and cursor < len(a_f):
			# print('on cursor', cursor)
			visted.add(cursor)
			inst, arg = a_f[cursor]
			# print(cursor, inst, arg)
			if inst == 'nop':
				cursor += 1
			elif inst == 'acc':
				acc += arg
				cursor += 1
			elif inst == 'jmp':
				cursor += arg
			else:
				raise 'oh no!'

		return (acc, cursor, cursor == len(a_f))

	fs = []
	for ind, x in enumerate(f):
		if x[0] == 'jmp':
			new_f = f.copy()
			new_f[ind] = ('nop', f[ind][1])
			fs.append(new_f)
		elif x[0] == 'nop':
			new_f = f.copy()
			new_f[ind] = ('jmp', f[ind][1])
			fs.append(new_f)

	# print(len(fs))

	for a_f in fs:
		acc, cursor, success = try_it(a_f)
		if success:
			print(acc)
			return

part_2()





