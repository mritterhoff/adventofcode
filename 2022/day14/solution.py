f = [x for x in open("input.txt").read().strip().split('\n')]
SANDCHAR = 'o'
ROCKCHAR = '#'

def printDic(dic, maxX, maxY, sandLoc = None):	
	for y in range(0, maxY + 1):
		line = " "
		for x in range(450, maxX + 10):
			if sandLoc == (x,y): line += dic.get((x,y), "X")	
			else: line += dic.get((x,y), " ")
		print(line)

def createDic(part2):
	dic = {}
	maxX, maxY = 0, 0
	for i, line in enumerate(f):
		pts = line.split(' -> ')

		for ii,pt in enumerate(pts):
			x,y = pt.split(',')
			x,y = int(x), int(y)
			maxX, maxY = max(maxX, x), max(maxY, y)
			
			if ii == 0:
				lastPt = (x, y)
			else:
				newPt = (x, y)
				if newPt[0] == lastPt[0]:
					ys = sorted([newPt[1], lastPt[1]])
					for y in range(ys[0], ys[1]+1):
						dic[(newPt[0], y)] = ROCKCHAR
				else:
					xs = sorted([newPt[0], lastPt[0]])
					for x in range(xs[0], xs[1]+1):
						dic[(x, newPt[1])] = ROCKCHAR
				lastPt = newPt
	if part2:
		maxY += 2
		for x in range(0, 1000): dic[(x, maxY)] = ROCKCHAR
	return [maxX, maxY, dic]

def canMove(dic, sandLoc, thisAction):
	if thisAction == 'd':
		sandLoc = (sandLoc[0], sandLoc[1]+1)
	elif thisAction == 'dl':
		sandLoc = (sandLoc[0]-1, sandLoc[1]+1)
	else:
		sandLoc = (sandLoc[0]+1, sandLoc[1]+1)
	return dic.get(sandLoc, 0) == 0

def solve(part2 = False):
	maxX, maxY, dic = createDic(part2)
	while True:
		sandPt = (500, 0)

		while canMove(dic, sandPt, 'd') or canMove(dic, sandPt, 'dl') or canMove(dic, sandPt, 'dr'):
			if canMove(dic, sandPt, 'd'):    thisAction = 'd'
			elif canMove(dic, sandPt, 'dl'): thisAction = 'dl'
			elif canMove(dic, sandPt, 'dr'): thisAction = 'dr'
			if thisAction:
				if thisAction == 'd':    sandPt = (sandPt[0],   sandPt[1]+1)
				elif thisAction == 'dl': sandPt = (sandPt[0]-1, sandPt[1]+1)
				elif thisAction == 'dr': sandPt = (sandPt[0]+1, sandPt[1]+1)

				if sandPt[1] > maxY:
					return len([x for x in dic.values() if x == SANDCHAR])
				else: continue 
		dic[sandPt], thisAction = SANDCHAR, None
		if sandPt == (500, 0):
			return len([x for x in dic.values() if x == SANDCHAR])
print('p1',solve())
print('p2',solve(True))
