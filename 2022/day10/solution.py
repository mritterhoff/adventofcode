import sys 
sys.path.append('../..')
from utils import *

# multiple lines
f = [x for x in open("test.txt").read().strip().split('\n')]

print(f)



insts = []

regX = 1
t = -1

total = 0



def solve(t, line, regX, total):

	if line == 'noop':
		# do nothing
		t+=1

		val = regX*t
		if t == 20:
			total += val
			print('val at', t, 'is', val, 'regx', regX)
		if t == 60:
			total += val
			print('val at', t, 'is', val, 'regx', regX)
		if t == 100:
			total += val
			print('val at', t, 'is', val, 'regx', regX)
		if t == 140:
			total += val
			print('val at', t, 'is', val, 'regx', regX)
		if t == 180:
			total += val
			print('val at', t, 'is', val, 'regx', regX)
		if t == 220:
			total += val
			print('val at', t, 'is', val, 'regx', regX)

		pass
	elif line:
		command, val = line.split(' ')
		val = int(val)
		insts.append([command, val, 2])
		t += 1

		val = regX*t
		if t == 20:
			total += val
			print('val at', t, 'is', val, 'regx', regX)
		if t == 60:
			total += val
			print('val at', t, 'is', val, 'regx', regX)
		if t == 100:
			total += val
			print('val at', t, 'is', val, 'regx', regX)
		if t == 140:
			total += val
			print('val at', t, 'is', val, 'regx', regX)
		if t == 180:
			total += val
			print('val at', t, 'is', val, 'regx', regX)
		if t == 220:
			total += val
			print('val at', t, 'is', val, 'regx', regX)

		popme = []
		for idx, inst in enumerate(insts):
			# print('insts', len(insts))
			if inst[0] == 'addx':
				inst[2] -= 1
				if inst[2] == 0:
					print('adding', inst[1])
					regX += inst[1]
					popme.append(idx)
		
		for x in popme:
			insts.pop(x)

		val = regX*t
		if t == 20:
			total += val
			print('val at', t, 'is', val, 'regx', regX)
		if t == 60:
			total += val
			print('val at', t, 'is', val, 'regx', regX)
		if t == 100:
			total += val
			print('val at', t, 'is', val, 'regx', regX)
		if t == 140:
			total += val
			print('val at', t, 'is', val, 'regx', regX)
		if t == 180:
			total += val
			print('val at', t, 'is', val, 'regx', regX)
		if t == 220:
			total += val
			print('val at', t, 'is', val, 'regx', regX)

	
	# print('insts',insts)
	# print('regx',regX)

	return t, regX, total

for line in f:
	t, regX, total = solve(t, line, regX, total)


# while len(insts) > 0:
# 	t, regX, total = solve(t, None, regX, total)


print("DONE")
print('regx', regX)
print('total',total)



# 94 not it



























