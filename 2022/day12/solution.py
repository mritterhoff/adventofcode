import sys 
sys.path.append('../..')
from utils import *

f = [x for x in open("input.txt").read().strip().split('\n')]

grid = []

for row in f:
	line = [x for x in row]
	grid.append(line)

grid = np.asarray(grid)

print(grid)

s, e = 0, 0

for r in range(grid.shape[0]):
	for c in range(grid.shape[1]):
		if grid[r][c] == 'S':
			s = (r, c)
		if grid[r][c] == 'E':
			e = (r, c)
print(s, e)

charList = list(string.ascii_letters)

def ns_4(p, R, C):
	y,x = p
	dirs = [(1,0), (-1,0), (0,1), (0,-1)]  # right/left/up/down
	out = [(y+dy, x+dx) for dy,dx in dirs if 0<= x+dx < C and 0<= y+dy < R]
	return out

minLen = 100000
shortPath = []

def getAllPaths(path, curR, curC):
	global minLen
	global shortPath
	# print('path so far', path)
	rez=[]
	cur_node = path[-1]

	if grid[curR][curC] == 'E':
		# print('we found it!', curR, curC)
		# print(path)
		if len(path) < minLen:
			shortPath = path
			minLen = len(path)
			print('minLen')
		return [path]

	nextNodes = ns_4((curR, curC), grid.shape[0], grid.shape[1])
	# print((curR, curC), nextNodes)
	for nextNode in nextNodes:
		# print('searching', nextNode)
		if grid[nextNode[0]][nextNode[1]] == 'S': continue

		nextHeight = charList.index('z') if grid[nextNode[0]][nextNode[1]] == 'E' else charList.index(grid[nextNode[0]][nextNode[1]])
		startHeight = charList.index('a') if grid[nextNode[0]][nextNode[1]] == 'S' else charList.index(grid[curR][curC])
		if nextHeight > startHeight + 1:
			continue

		if nextNode in path: continue
		subPath = copy.deepcopy(path)
		subPath.append(nextNode)
		getAllPaths(subPath, nextNode[0], nextNode[1])

getAllPaths([s], s[0], s[1])

print(shortPath)
print(len(shortPath)-1)




# raise


# state = np.asarray([[int(el) for el in row] for row in f])
# print(state)

# R,C = state.shape
# print('rows:', R, ' cols:', C)

# hist = [state]
# for gen in range(0, 2):
# 	print('gen:', gen+1)
# 	old = hist[-1]
# 	new = np.full((R,C), 0)

# 	for iy in range(R):
# 		for ix in range(C):
# 			 for pt in ns_8((ix, iy), R, C):
# 		 	pp(pt)

# 	hist.append(new)
# 	pp(old)
# 	pp(new)



# raise
# print(f)

# nodes = set()
# edges = defaultdict(list)

# for x in f:
# 	a, b = x.split('-')
# 	nodes.add(a)
# 	nodes.add(b)
# 	edges[a].append(b)
# 	edges[b].append(a)

# print(nodes)
# print(edges)

# def getAllPaths(path, startNodeName, endNodeName):
# 	rez=[]
# 	cur_node = path[-1]

# 	if cur_node == endNodeName: return [path]

# 	for nextNode in edges[cur_node]:
# 		if nextNode == startNodeName: continue
# 		if nextNode in path: continue
# 		subPath = copy.deepcopy(path)
# 		subPath.append(nextNode)
# 		rez.extend(getAllPaths(subPath, startNodeName, endNodeName))

# 	return rez

# pp(getAllPaths(['start'], 'start', 'end'))































