from parse import *

f = [x for x in open("input.txt").read().strip().split('\n')]

def manDist(t1, t2):
	return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])

sens = []
dists = []
notHere = {}
for line in f:
	senX, senY, bX, bY = parse("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", line)
	dist = manDist((senX, senY), (bX, bY))

	sen = (senX, senY)
	dists.append(dist)
	sens.append(sen)
	for x in range(senX-dist-1, senX+dist+1):
		y = 2000000
		if manDist((x,y), sen) <= dist:
			notHere[(x,y)] = 'x'

print('p1:', len(notHere)-1)

max = 4000000
def checkDistToSensors(x,y):
	for i in range(len(sens)):
		if manDist((x,y), sens[i]) <= dists[i]: return False
	return x*4000000+y

bounds = set()
p2Answer = False

for i in range(0, len(sens)):
	xdiff,ydiff = dists[i]+1, 0
	while xdiff >=0 and not p2Answer:
		sX,sY = sens[i][0], sens[i][1]
		options = [
			[sX + xdiff, sY + ydiff],
			[sX - xdiff, sY + ydiff],
			[sX + xdiff, sY - ydiff],
			[sX - xdiff, sY - ydiff]
		]
		
		for x,y in options:
			if 0<=x<=max and 0<=y<=max:
				p2Answer = checkDistToSensors(x, y)
				if p2Answer: break
		xdiff -= 1
		ydiff += 1
	if p2Answer: break

print('p2:', p2Answer)













