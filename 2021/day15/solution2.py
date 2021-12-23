import pprint
import heapq as hq
from functools import cache
from termcolor import colored

lines = [x for x in open("input.txt").read().strip().split('\n')]


G = []
for line in lines:
	G.append([int(x) for x in line])

R = len(G)
C = len(G[0])

realG = []
for gr in range(R*5):
	row = []
	for gc in range(C*5):
		r = gr % R
		c = gc % C
		inc = (gr // R) + (gc // C)
		gVal = (G[r][c] + inc -1 ) % 9 +1

		row.append(gVal)
	realG.append(row)

G = realG
R = len(G)
C = len(G[0])

start = (0,0)
goal = (C-1,R-1)

out = []
for r in range(R):
	row = []
	for c in range(C):
		row.append(str(G[r][c]))
	out.append("".join(row))
# pprint.pp(out)

inf = float('inf') 

def printSet(s):
	for r in range(R):
		row = []
		for c in range(C):
			if (c,r) in s:
				row.append(str(G[r][c]))
			else:
				row.append(' ')
		print("".join(row))

@cache
def neighbors(p):
	x,y = p
	dirs = [(1,0), (0,1), (-1,0), (0,-1)]
	ns = []
	for dx,dy in dirs:
		if 0<= x+dx < C and 0<= y+dy < R:
			ns.append((x+dx, y+dy))
	return ns

@cache
def h(can):
	return 0
	# return abs(goal[1] - can[1]) + abs(goal[0] - can[0])
	

def d(current, neighbor):
	return G[neighbor[1]][neighbor[0]]

# current := the node in openSet having the lowest fScore[] value
def smallestF(fScore,openSet):
	minF = inf
	minN = None
	# print(openSet)
	for n in openSet:
		score = fScore.get(n, inf)
		if score < minF:
			minF = score
			minN = n
	# print(f"smallestF returning with {minN} (score {score}) after searching {openSet}")
	return n

def print_everything(total_path, lookedat, current=None):
	for r in range(R):
		row = []
		for c in range(C):
			color = None
			if (c,r) == current:
				color = 'red'
			elif (c,r) in total_path:
				color = 'green'
			elif (c,r) in lookedat:
				color = 'white'
			else:
				color = 'blue'
		print(colored(str(G[r][c]), color), end='')
		print()

def reconstruct_path(cameFrom, current):
	total_path = [current]
	while current in cameFrom.keys():
		current = cameFrom[current]
		total_path.insert(0, current)
	return total_path

lookedat = set()
def a_star(start, goal):
	openSet = []
	hq.heappush(openSet, (h(start), start))
	cameFrom = {}

	# the cost of the cheapest path from start to n currently known.
	gScore = {}
	gScore[start] = 0
	
	fScore={}
	fScore[start] = h(start)

	cycle = 0
	while len(openSet) > 0:
		s, current = hq.heappop(openSet)
		if current == goal:
			return reconstruct_path(cameFrom, current)

		ns = neighbors(current)

		for neighbor in ns:
			tentative_gScore = gScore[current] + d(current, neighbor)

			# This path to neighbor is better than any previous one. Record it!
			if tentative_gScore < gScore.get(neighbor, inf):
				cameFrom[neighbor] = current
				gScore[neighbor] = tentative_gScore
				fScore[neighbor] = tentative_gScore + h(neighbor)
				if neighbor not in [y for x,y in openSet]:
					hq.heappush(openSet, (fScore[neighbor], neighbor))
					lookedat.add(neighbor)
		cycle += 1
		if cycle % 10000 == 0: print(cycle)

	print('we failed')

total_path = a_star(start, goal)

print_everything(total_path, lookedat)


print(sum([G[y][x] for x,y in total_path if (x,y) != start]))


