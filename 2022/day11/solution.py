import sys 
sys.path.append('../..')
from utils import *

# multiple lines
f = [x for x in open("input.txt").read().strip().split('\n\n')]

# p1 35
inspectCount = defaultdict(int)
monkeys = {}

def parseMonkeys(str):
	global monkeys
	lines = str.split('\n')

	monk = {}
	monk['list'] = [int(x) for x in lines[1].split(':')[1].split(',')]

	monk['op'] = [x for x in parse('  Operation: new = {} {} {}', lines[2])]

	monk['divTest'] = parse('  Test: divisible by {:d}', lines[3])[0]

	monk['divTrue'] = parse('    If true: throw to monkey {:d}', lines[4])[0]
	monk['divFalse'] = parse('    If false: throw to monkey {:d}', lines[5])[0]

	monkeys[len(monkeys)] = monk

def monkInspect(curMonkIdx):
	monk =  monkeys[curMonkIdx]
	
	for el in monk['list']:
		el = doOp(el, monk['op'])
		el = el // 3 #p1 only

		if el / monk['divTest'] == el // monk['divTest']:
			monkeys[monk['divTrue']]['list'].append(el)
		else:
			monkeys[monk['divFalse']]['list'].append(el)

		inspectCount[curMonkIdx] += 1


	monk['list'] = []



def doOp(old, op):
	if op[2] == 'old':
		return old*old
	else:
		if op[1] == '+':
			return old + int(op[2])
		return old * int(op[2])


for monkStr in f:
	parseMonkeys(monkStr)

for rnd in range(0, 20):
	for mIdx in range(len(monkeys)):
		monkInspect(mIdx)


pp(monkeys)
s = list(reversed(sorted(inspectCount.values())))
pp(s[0] * s[1])






































