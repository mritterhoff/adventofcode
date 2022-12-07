from utils import *

f =[x for x in open("sample_input/node_pairs.txt").read().strip().split('\n')]

print(f)

nodes = set()
edges = defaultdict(list)

for x in f:
	a, b = x.split('-')
	nodes.add(a)
	nodes.add(b)
	edges[a].append(b)
	edges[b].append(a)

print(nodes)
print(edges)

def getAllPaths(path, startNodeName, endNodeName):
	rez=[]
	cur_node = path[-1]

	if cur_node == endNodeName: return [path]

	for nextNode in edges[cur_node]:
		if nextNode == startNodeName: continue
		if nextNode in path: continue
		subPath = copy.deepcopy(path)
		subPath.append(nextNode)
		rez.extend(getAllPaths(subPath, startNodeName, endNodeName))

	return rez

pp(getAllPaths(['start'], 'start', 'end'))
