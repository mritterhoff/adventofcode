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

def getAllPaths(path, curR, curC):
	global minLen
	rez=[]
	cur_node = path[-1]

	if grid[curR][curC] == 'E':
		if len(path) < minLen:
			minLen = len(path)
			print('minLen', minLen)
		# return [path]

	nextNodes = ns_4((curR, curC), grid.shape[0], grid.shape[1])
	for nextNode in nextNodes:
		if grid[nextNode[0]][nextNode[1]] == 'S': continue
		if nextNode in path: continue
		nextHeight = charList.index('z') if grid[nextNode[0]][nextNode[1]] == 'E' else charList.index(grid[nextNode[0]][nextNode[1]])
		startHeight = charList.index('a') if grid[nextNode[0]][nextNode[1]] == 'S' else charList.index(grid[curR][curC])
		if nextHeight > startHeight + 1:
			continue

		
		path.append(nextNode)
		getAllPaths(path, nextNode[0], nextNode[1])
		path.pop()

getAllPaths([s], s[0], s[1])

# print(shortPath)
print(minLen-1)


