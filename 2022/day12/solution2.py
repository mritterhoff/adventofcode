import pprint
import heapq as hq
from functools import cache
from termcolor import colored
import string

lines = [x for x in open("input.txt").read().strip().split('\n')]

G = [[x for x in line] for line in lines]

print(G)
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

	return 1
	# return G[neighbor[1]][neighbor[0]]

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

charList = list(string.ascii_letters)

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
			nextHeight = charList.index('z') if G[neighbor[1]][neighbor[0]] == 'E' else charList.index(G[neighbor[1]][neighbor[0]])
			startHeight = charList.index('a') if G[neighbor[1]][neighbor[0]] == 'S' else charList.index(G[current[1]][current[0]])
			if nextHeight > startHeight + 1:
				continue

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

# start, goal = None, None

# for r in range(R):
# 	for c in range(C):
# 		if G[r][c] == 'S':
# 			start = (c, r)
# 		if G[r][c] == 'E':
# 			goal = (c, r)

# print(start, goal)
# total_path = a_star(start, goal)


# print(len(total_path)-1)

starts, goal = [], None
for r in range(R):
	for c in range(C):
		if G[r][c] == 'a' or G[r][c] == 'S':
			starts.append((c, r))
		if G[r][c] == 'E':
			goal = (c, r)


print(starts, goal)
best = 10000000
for start in starts:
	total_path = a_star(start, goal)
	# print(total_path)
	if total_path and len(total_path) -1 < best:
		best = len(total_path) -1
		print(best)






