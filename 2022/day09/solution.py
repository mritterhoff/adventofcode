f = [[x.split(' ')[0], int(x.split(' ')[1])] for x in open("input.txt").read().strip().split('\n')]

dirs = { 
  'R': (1, 0), 
  'L': (-1, 0),
  'U': (0, 1),
  'D': (0, -1)
}

def sign(v):
	return 0 if v == 0 else int((v)/abs(v)) 

def manDist(t1, t2):
	return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])

def addTupes(t1, t2):
	return (t1[0] + t2[0], t1[1] + t2[1])

def solve(knotCount):
	tailWasHere = set()
	knotCoord = dict([(x, (0,0)) for x in range(knotCount)])

	for d, s in f:
		for _ in range(s):
			for k in range(knotCount-1):
				thisKnot, nextKnot = knotCoord[k], knotCoord[k+1]
				
				if k == 0:
					thisKnot = addTupes(thisKnot, dirs[d])
					knotCoord[k] = thisKnot

				if manDist(thisKnot, nextKnot) >= 2:
					moveX, moveY = 0, 0
					if thisKnot[0] == nextKnot[0] or thisKnot[1] == nextKnot[1]:
						moveX = sign(thisKnot[0] - nextKnot[0])
						moveY = sign(thisKnot[1] - nextKnot[1])
					else:
						if manDist(thisKnot, nextKnot) > 2:
							moveX = sign(thisKnot[0] - nextKnot[0])
							moveY = sign(thisKnot[1] - nextKnot[1])
					nextKnot = addTupes(nextKnot, (moveX, moveY))
				
				knotCoord[k+1] = nextKnot
				if k == knotCount-2: tailWasHere.add(nextKnot)
	return len(tailWasHere)

print('p1:',solve(2))
print('p2:',solve(10))