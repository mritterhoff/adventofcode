import math
import re

f = [x for x in open("input.txt").read().strip().split('\n')]

def add_line(rec, line):
	rec.update({x: y for x,y in [x.split(':') for x in line.split(' ')]})

def is_valid(rec, part2=False):
	part1_valid = len(set(rec.keys()) & set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'])) == 7 
	if not part2 :
		return part1_valid

	def hgt(x):
		if len(x)<4:
			return False
		last2 = x[-2:]
		num = int(x[:-2])
		if last2 == 'cm':
			return 150 <= num <= 193
		elif last2 == 'in':
			return 59 <= num <= 76
		else:
			return False

	funcs = {
		"byr": lambda x: 1920 <= int(x) <= 2002,
		"iyr": lambda x: 2010 <= int(x) <= 2020,
		"eyr": lambda x: 2020 <= int(x) <= 2030,
		"hgt": lambda x: hgt(x),
		"hcl": lambda x: re.match('^#[0-9a-f]{6}$', x),
		"ecl": lambda x: x in 'amb blu brn gry grn hzl oth'.split(' '),
		"pid": lambda x: re.match('^[0-9]{9}$', x),
		"cid": lambda x: True,
	}

	if not part1_valid:
		return False

	rez = {}
	for func in sorted(rec.keys()):
		rez[func] = bool(funcs[func](rec[func]))
	return False not in rez.values()

def do_it(part2=False):
	count, rec = 0, None

	for line in f:
		if rec == None:
			rec = {}
		if len(line) == 0:
			if is_valid(rec, part2):
				count += 1
			rec = None
		else:
			add_line(rec, line)

	print(count)

do_it()
do_it(True)
