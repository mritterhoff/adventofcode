import pprint
import heapq as hq
from functools import cache
from termcolor import colored

lines = [x for x in open("sample_input/big_number_grid.txt").read().strip().split('\n')]

G = [[int(x) for x in line] for line in lines]
inf = float("inf")

@cache
def neighbors(p):
	x,y = p
	ns = []
	for dx,dy in [(1,0), (0,1), (-1,0), (0,-1)]:
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
	for n in openSet:
		score = fScore.get(n, inf)
		if score < minF:
			minF = score
			minN = n
	return n

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

		for neighbor in neighbors(current):
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


R = len(G)
C = len(G[0])
start = (0,0)
goal = (C-1,R-1)
total_path = a_star(start, goal)


print(sum([G[y][x] for x,y in total_path if (x,y) != start]))


# 626 for this new smaller version

