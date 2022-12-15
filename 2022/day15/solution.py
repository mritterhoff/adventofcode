from parse import *

f = [x for x in open("input.txt").read().strip().split('\n')]

def manDist(t1, t2):
	return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])

sensorToDist = {}
notHere = set()
for line in f:
	senX, senY, bX, bY = parse("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", line)
	dist = manDist((senX, senY), (bX, bY))

	sen = (senX, senY)
	sensorToDist[sen] = dist
	for x in range(senX-dist-1, senX+dist+1):
		y = 2000000
		if manDist((x,y), sen) <= dist: notHere.add((x,y))

print('p1:', len(notHere)-1) # why -1?

max = 4000000
def checkDistToSensors(x,y):
	for sensor,dist in sensorToDist.items():
		if manDist((x,y), sensor) <= dist: return False
	return x*4000000+y

p2Answer = False
for sensor,dist in sensorToDist.items():
	xdiff,ydiff = dist+1, 0
	while xdiff >=0 and not p2Answer:
		for signX,signY in [[1,1], [1,-1], [-1,-1], [1, 1]]:
			x = sensor[0] + xdiff*signX
			y = sensor[1] + ydiff*signY
			if 0<=x<=max and 0<=y<=max:
				p2Answer = checkDistToSensors(x, y)
				if p2Answer: break
		xdiff -= 1
		ydiff += 1
	if p2Answer: break

print('p2:', p2Answer)

