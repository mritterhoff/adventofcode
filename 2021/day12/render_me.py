from pprint import pprint
import math
import numpy as np
import copy
import collections

import networkx as nx
import matplotlib.pyplot as plt

f =[x for x in open("test.txt").read().strip().split('\n')]
# f = np.asarray([[int(y) for y in x] for x in f])

print(f)

nodes = set()
edges = {}

# .isupper()
# copy.deepcopy(a)
# list1.extend(list2)

def would_have_to_many_smalls(path, n):
	c = {}
	for x in path:
		if x.islower():
			if x in c:
				c[x] += 1
			else:
				c[x] = 1
	x = n
	if x.islower():
		if x in c:
			c[x] += 1
		else:
			c[x] = 1

	most_pop = [x for x in c.values() if x > 1]

	rez = True
	if len(most_pop) == 1 and most_pop[0] == 2:
		rez = False

	# print('in whtms:',path, n, rez)
	return rez


def add_edge(a, b):
	if a not in edges:
		edges[a] = [b]
	else:
		edges[a].append(b)

	if b not in edges:
		edges[b] = [a]
	else:
		edges[b].append(a)

for x in f:
	a, b = x.split('-')
	nodes.add(a)
	nodes.add(b)
	add_edge(a,b)

print(nodes)
print(edges)


paths = []

# def explore(path):
# 	rez=[]
# 	cur_node = path[-1]

# 	if cur_node == 'end':
# 		return [path]

# 	for n in edges[cur_node]:
# 		if n in path and n.islower():
# 			continue

# 		p = copy.deepcopy(path)
# 		p.append(n)
# 		rez.extend(explore(p))

# 	return rez

def explore(path):
	rez=[]
	cur_node = path[-1]

	# if len(path) > 10:
	# 	return rez

	if cur_node == 'end':
		return [path]

	for n in edges[cur_node]:
		if n == 'start':
			continue
		if n in path and n.islower() and would_have_to_many_smalls(path, n):
			continue
		p = copy.deepcopy(path)
		p.append(n)
		rez.extend(explore(p))

	return rez


rez = explore(['start'])

for x in rez:
	print(x)

# # Defining a Class
# class GraphVisualization:
   
# 	def __init__(self):
		  
# 		# visual is a list which stores all 
# 		# the set of edges that constitutes a
# 		# graph
# 		self.e = []
		  
# 	# addEdge function inputs the vertices of an
# 	# edge and appends it to the visual list
# 	def addEdge(self, a, b):
# 		self.visual.append([a, b])
		  
# 	# In visualize function G is an object of
# 	# class Graph given by networkx G.add_edges_from(visual)
# 	# creates a graph with a given list
# 	# nx.draw_networkx(G) - plots the graph
# 	# plt.show() - displays the graph
# 	# def visualize(self):
# 	#	 G = nx.MultiDiGraph()
# 	#	 G.add_edges_from(self.visual)
# 	#	 nx.draw_networkx(G)
# 	#	 plt.show()

# 	# # basic, works ok	 
# 	# def visualize(self):
# 	# 	G = nx.Graph()
# 	# 	G.add_edges_from(self.visual)
# 	# 	pos = nx.spring_layout(G, seed=47) 
# 	# 	nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", pos=pos)
# 	# 	plt.show()

# 	def visualize(self):
# 		G = nx.Graph()
# 		G.add_edges_from(self.visual)



# 		pos = nx.spring_layout(G, seed=47) 
# 		nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", pos=pos)
# 		plt.show()


# G = GraphVisualization()
# for x in f:
# 	print('adding', x)
# 	a, b = x.split('-')
# 	G.addEdge(a,b, )
# G.visualize()


