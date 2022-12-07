import pprint
import heapq as hq
from functools import cache
from termcolor import colored

lines = [x for x in open("input.txt").read().strip().split('\n')]

G = []
for line in lines:
	G.append([int(x) for x in line])

start = (0,0)


R = len(G)
C = len(G[0])

goal = (C-1,R-1)

out = []
for r in range(R):
	row = []
	for c in range(C):
		row.append(str(G[r][c]))
	out.append("".join(row))
pprint.pp(out)



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
	# dirs = [(1,0), (0,1)]
	ns = []

	for dx,dy in dirs:
		if 0<= x+dx < C and 0<= y+dy < R:
			ns.append((x+dx, y+dy))
	return ns


@cache
def h(can):
	# return inf
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


# hq.heappop(heap)
# hq.heappush(heap, x)
# hq.heappush(heap, x)

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
	openSet = set(start)
	cameFrom = {}

	# the cost of the cheapest path from start to n currently known.
	gScore = {}
	gScore[start] = 0
	
	fScore={}
	fScore[start] = h(start)

	cycle = 0
	while len(openSet) > 0:
		# print('openSet',len(openSet))
		# printSet(openSet)

		#TODO This has to be broken
		current = smallestF(fScore,openSet)

		# if current[0] >= 9 and current[1] >= 9:
			# print('exploring...', current)
		if current == goal:
			print("WE DID IT")
			
			return reconstruct_path(cameFrom, current)
		openSet.remove(current)

		ns = neighbors(current)
		# print(f"exploring neighors for {current} which are: {ns}")

		for neighbor in ns:
			tentative_gScore = gScore[current] + d(current, neighbor)
			# print(f"for {neighbor}, value is {G[neighbor[1]][neighbor[0]]} tentative_gScore is {tentative_gScore}")
			# print_everything(reconstruct_path(cameFrom, current), lookedat, neighbor)
			if tentative_gScore < gScore.get(neighbor, inf):

				# This path to neighbor is better than any previous one. Record it!
				cameFrom[neighbor] = current
				gScore[neighbor] = tentative_gScore
				fScore[neighbor] = tentative_gScore + h(neighbor)
				if neighbor not in openSet:
					openSet.add(neighbor)
					lookedat.add(neighbor)
		cycle += 1
		# if cycle < 400 or cycle % 10000 == 0: print(cycle)

	print('we failed')



print('start, goal', start, goal)
total_path = a_star(start, goal)
print(lookedat)

# total_path = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (3, 5), (4, 5), (5, 5), (5, 6), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15), (12, 16), (12, 17), (13, 17), (13, 18), (13, 19), (14, 19), (14, 20), (15, 20), (15, 21), (16, 21), (16, 22), (16, 23), (16, 24), (17, 24), (17, 25), (17, 26), (17, 27), (18, 27), (19, 27), (19, 28), (20, 28), (21, 28), (21, 29), (21, 30), (22, 30), (23, 30), (24, 30), (25, 30), (25, 31), (25, 32), (26, 32), (27, 32), (28, 32), (28, 33), (29, 33), (30, 33), (31, 33), (32, 33), (32, 34), (33, 34), (33, 35), (33, 36), (34, 36), (34, 37), (35, 37), (35, 38), (36, 38), (36, 39), (37, 39), (38, 39), (39, 39), (40, 39), (40, 40), (41, 40), (41, 41), (42, 41), (42, 42), (42, 43), (42, 44), (42, 45), (42, 46), (41, 46), (41, 47), (41, 48), (41, 49), (41, 50), (41, 51), (42, 51), (42, 52), (43, 52), (44, 52), (45, 52), (46, 52), (46, 53), (47, 53), (48, 53), (49, 53), (50, 53), (51, 53), (51, 54), (51, 55), (52, 55), (52, 56), (53, 56), (53, 57), (53, 58), (54, 58), (55, 58), (55, 59), (55, 60), (56, 60), (56, 61), (56, 62), (56, 63), (57, 63), (58, 63), (59, 63), (59, 64), (59, 65), (60, 65), (61, 65), (61, 66), (62, 66), (62, 67), (63, 67), (63, 68), (64, 68), (65, 68), (66, 68), (67, 68), (67, 69), (67, 70), (68, 70), (68, 71), (68, 72), (69, 72), (70, 72), (70, 73), (70, 74), (70, 75), (71, 75), (71, 76), (72, 76), (72, 77), (72, 78), (72, 79), (72, 80), (72, 81), (72, 82), (73, 82), (74, 82), (74, 83), (74, 84), (74, 85), (75, 85), (76, 85), (76, 86), (77, 86), (77, 87), (78, 87), (78, 88), (78, 89), (79, 89), (80, 89), (81, 89), (82, 89), (82, 90), (83, 90), (83, 91), (84, 91), (84, 92), (85, 92), (85, 93), (85, 94), (86, 94), (87, 94), (88, 94), (89, 94), (89, 95), (90, 95), (91, 95), (92, 95), (93, 95), (94, 95), (95, 95), (96, 95), (96, 96), (97, 96), (97, 97), (97, 98), (98, 98), (99, 98), (99, 99)]

print(total_path)





print(sum([G[y][x] for x,y in total_path if (x,y) != start]))


# 798 is too high! 790 also too high, so is 780

# not 871 (duh)










