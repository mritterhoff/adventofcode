import sys 
sys.path.append('../..')
from utils import *
import inspect

# multiple lines
f = [x for x in open("input.txt").read().strip().split('\n\n')]

# p1 35, p2 clock 2:24t

class N1:
	def __init__(self, num):
		self.map = {}

		for c in [17,13,19,23,5,2,7,11,3]:
			self.map[c] = num % c

	def plus(self, num):
		for c in self.map.keys():
			self.map[c] = (self.map[c] + num) % c

	def test(self, num):
		return self.map[num] == 0

	def mult(self, num):
		for c in self.map.keys():
			self.map[c] = (self.map[c] * num) % c

	def multSelf(self):
		for c in self.map.keys():
			self.map[c] = (self.map[c] * self.map[c]) % c


def doOp(old, op):
	if op[2] == 'old':
		return old*old
	else:
		if op[1] == '+':
			return old + op[2]
		return old * op[2]

def doOp2(old, op):
	if op[2] == 'old':
		old.multSelf()
	else:
		if op[1] == '+':
			old.plus(op[2])
		else:
			old.mult(op[2])


def parseMonkeys(str):
	global monkeys
	global part
	lines = str.split('\n')

	monk = {}
	
	if part == 'p1':
		monk['list'] = [int(x) for x in lines[1].split(':')[1].split(',')]
	else:
		monk['list'] = [N1(int(x)) for x in lines[1].split(':')[1].split(',')]

	monk['op'] = [x for x in parse('  Operation: new = {} {} {}', lines[2])]
	if monk['op'][2] != 'old':
		monk['op'][2] = int(monk['op'][2])

	monk['divTest'] = parse('  Test: divisible by {:d}', lines[3])[0]

	monk['divTrue'] = parse('    If true: throw to monkey {:d}', lines[4])[0]
	monk['divFalse'] = parse('    If false: throw to monkey {:d}', lines[5])[0]

	monkeys[len(monkeys)] = monk


def solve(rounds):
	global part
	for monkStr in f: parseMonkeys(monkStr)

	for rnd in range(rounds):
		for mIdx in range(len(monkeys)):
			monk = monkeys[mIdx]
			while (len(monk['list']) > 0):
				el = monk['list'].pop()
				
				if part == 'p1':
					el = doOp(el, monk['op']) // 3
					testPassed = el % monk['divTest'] == 0
				else:
					doOp2(el, monk['op'])
					testPassed = el.test(monk['divTest'])

				if testPassed:
					monkeys[monk['divTrue']]['list'].append(el)
				else:
					monkeys[monk['divFalse']]['list'].append(el)

				inspectCount[mIdx] += 1

	s = list(reversed(sorted(inspectCount.values())))
	print(part, s[0] * s[1])

worryList = []

inspectCount = defaultdict(int)
monkeys = {}
part = 'p1'
solve(20)

worryList = []

inspectCount = defaultdict(int)
monkeys = {}
part = 'p2'
solve(10000)



