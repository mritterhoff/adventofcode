import copy
from collections import defaultdict, Counter
from parse import *


def solve(p1 = True):	
	grid, insts = [x for x in open("input.txt").read().split('\n\n')]
	grid = [x for x in grid.split('\n')]
	insts = [x for x in insts.strip().split('\n')]

	col_lookup = {}
	state = defaultdict(list)
	for idx, row in enumerate(reversed(grid)):
		if idx == 0:
			for x in [int(x) for x in row if x != ' ']: 
				col_lookup[x] = row.index(str(x))
		else:
			for num,look_here in col_lookup.items():
				if row[look_here] != ' ':
					state[num].append(row[look_here])

	hist = [state]
	for inst in insts:
		rows = copy.deepcopy(hist[-1])
		amount, fm, to = parse("move {:d} from {:d} to {:d}", inst)
		rows[fm], more = rows[fm][:-amount], rows[fm][-amount:]

		if p1: more.reverse()
		rows[to] += more
		
		hist.append(rows)

	out = ""
	for k,y in hist[-1].items():
		if len(y) > 0: out += y[-1]
	print("p1:" if p1 else "p2:", out)


solve(True)
solve(False)













































