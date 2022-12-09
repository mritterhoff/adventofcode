# https://adventofcode.com/2022/day/8

import numpy as np

f = [x for x in open("input.txt").read().strip().split('\n')]
trees = np.array([[int(x) for x in ff] for ff in f])

def scoreP2(v, arr):
	for i, el in enumerate(arr):
		if el >= v: return i + 1
	return len(arr)

p1, p2 = 2*(trees.shape[0] + trees.shape[1]) - 4, 0 
for x in range(1, trees.shape[0]-1):
	for y in range(1, trees.shape[1]-1):
		score1 = trees[y][x] > max(trees[y,:x])
		score1 |= trees[y][x] > max(trees[y,x+1:])
		score1 |= trees[y][x] > max(trees[:y,x])
		score1 |= trees[y][x] > max(trees[y+1:,x])
		p1 += 1 if score1 else 0

		score2 = scoreP2(trees[y][x], list(reversed(trees[y,:x])))
		score2 *= scoreP2(trees[y][x], trees[y,x+1:])
		score2 *= scoreP2(trees[y][x], list(reversed(trees[:y,x])))
		score2 *= scoreP2(trees[y][x], trees[y+1:,x])
		p2 = max(p2, score2)

print('p1:', p1)
print('p2:', p2)