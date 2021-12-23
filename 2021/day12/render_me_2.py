from pprint import pprint
import math
import numpy as np
import copy
import collections
import os
import shutil

import networkx as nx
import matplotlib.pyplot as plt

f =[x for x in open("test.txt").read().strip().split('\n')]
# f = np.asarray([[int(y) for y in x] for x in f])

print(f)

nodes = set()
edges = {}

gen = 0

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

g_edges = [x.split('-') for x in f]


paths = []


def explore(path):
	rez=[]
	cur_node = path[-1]

	if cur_node == 'end':
		draw_with_path(path)
		return [path]

	draw_with_path(path)
	for n in edges[cur_node]:
		if n == 'start': continue
		if n in path and n.islower() and would_have_to_many_smalls(path, n): continue
		draw_with_path(path)
		p = copy.deepcopy(path)
		p.append(n)

		draw_with_path(p)

		rez.extend(explore(p))

	draw_with_path(path)
	return rez

def edge_from_pair(G, p):
	if p in list(G.edges):
		return p
	return (p[1], p[0])


def draw_with_path(path):
	G = nx.Graph()
	G.add_edges_from(g_edges)

	# print ('g edges',list(G.edges))
	# edges = list(G.edges)[0:3]

	edges = []
	edge_name_to_count = {}
	for e in zip(path[:-1],path[1:]):
		name = "".join(sorted(e))
		edge_name_to_count[name] = edge_name_to_count.get(name, 0) + 1

	# print(edge_name_to_count)

	edge_weights = []
	for e in zip(path[:-1],path[1:]):
		name = "".join(sorted(e))
		edge_weights.append([edge_from_pair(G, e), edge_name_to_count[name]])

	# print('edge_weights', edge_weights)

	unvisted_nodes = []
	visted_nodes = []
	cur_node = path[-1]
	for n in G.nodes():
		if n != cur_node:
			if n in path: visted_nodes.append(n)
			else: unvisted_nodes.append(n)


	options = {"edgecolors": "tab:gray", "node_size": 1500, "alpha": 0.95}
	pos = nx.spring_layout(G, seed=47) 
	nx.draw_networkx_nodes(G, pos, nodelist=unvisted_nodes, node_color="tab:red", **options)
	nx.draw_networkx_nodes(G, pos, nodelist=visted_nodes, node_color="tab:blue", **options)
	nx.draw_networkx_nodes(G, pos, nodelist=[cur_node], node_color="tab:green", **options)

	# draw all edges very faintly to start
	nx.draw_networkx_edges(G, pos, width=.1, alpha=0.5)

	for x in edge_weights:
		edge = x[0]
		weight = max(2, x[1]**2)
		nx.draw_networkx_edges(G, pos, edgelist=[edge], width=weight, alpha=0.5)

	nx.draw_networkx_labels(G, pos, font_size=12, font_color="whitesmoke")
	DPI = 100
	global gen
	# plt.show()
	plt.box(False)
	plt.savefig(f"out/graph_{str(gen).zfill(5)}.png", dpi=DPI)
	plt.clf()
	gen += 1

# create/delete our temp files folder
if os.path.exists('out'):
    shutil.rmtree('out')
os.mkdir('out')


rez = explore(['start'])

# os.system('ffmpeg -framerate 24 -i out/graph_%05d.png -c:v ffv1 -r 24 -y out.avi')
# os.system('ffmpeg -y -i out.avi -vf palettegen palette.png')
# os.system('ffmpeg -y -i out.avi -i palette.png -lavfi paletteuse out/out.gif')
