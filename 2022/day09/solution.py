import sys 
sys.path.append('../..')
from utils import *

f = [x for x in open("input.txt").read().strip().split('\n')]

dirs = { 
  'R': (1, 0), 
  'L': (-1, 0),
  'U': (0, 1),
  'D': (0, -1)
  }

def getDir(v1, v2):
	return int((v1 - v2)/abs(v1 - v2))

def solve(count = 2):
	twh = set()
	knots = dict()

	for x in range(count):
		knots[x] = (0,0)

	for x in f:
		d, s = x.split(' ')
		s = int(s)
		for hstep in range(s):
			for k in range(count-1):
				h = knots[k]
				t = knots[k+1]
				
				if k == 0:
					h = (h[0] + dirs[d][0], h[1] + dirs[d][1])
					knots[k] = h

				mandist = abs(h[0] - t[0]) + abs(h[1] - t[1])
				if mandist >= 2:
					if h[0] == t[0]:
						t = (t[0], t[1] + getDir(h[1], t[1]))
					elif h[1] == t[1]:
						t = (t[0] + getDir(h[0], t[0]), t[1])
					else:
						if mandist > 2:
							dirx = getDir(h[0], t[0])
							diry = getDir(h[1], t[1])
							t = (t[0] + dirx, t[1]+diry)
				knots[k+1] = t

				if k == count-2: twh.add(knots[count-1])

	return len(list(twh))

print('p1',solve())
print('p2',solve(10))
