import numpy as np
import itertools

class Line:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def horiz(self):
		return self.p1[1] == self.p2[1]

	def vert(self):
		return self.p1[0] == self.p2[0]

	def diag(self):
		return abs((self.p1[0]-self.p2[0])/(self.p1[1]-self.p2[1])) == 1

	def all_points_with_diag(self, diag):
		if self.horiz():
			return [[x, self.p1[1]] for x in range(self.p1[0], self.p2[0] +1)]	+ [[x, self.p1[1]] for x in range(self.p2[0], self.p1[0] +1)]
		elif self.vert():
			return [[self.p1[0], y] for y in range(self.p1[1], self.p2[1] +1)]	+ [[self.p1[0], y] for y in range(self.p2[1], self.p1[1] +1)]	
		elif diag and self.diag():
			return self.diag_calc()
		else:
			return []

	def diag_calc(self):
		p1 = self.p1
		p2 = self.p2

		## switch if we need to so we can go left to right
		if (p1[0] > p2[0]):
			t = p1
			p1 = p2
			p2 = t

		# do we go up or down?
		up = p1[1] < p2[1]

		pts = []
		count = 0
		for x in range(p1[0], p2[0] + 1):
			pts.append([x, p1[1] + (count if up else -count)])
			count += 1
		return pts

	def __str__(self):
		return str(self.p1) + " " + str(self.p2)


f = [x.split(' -> ') for x in open("test.txt").read().strip().split("\n")]
lines = [Line(list(map(int, (p1.split(',')))), list(map(int, p2.split(',')))) for p1, p2 in f]

def part(include_diags):
	arr_of_arrs = [l.all_points_with_diag(include_diags) for l in lines]
	pts = list(itertools.chain.from_iterable(arr_of_arrs))

	d = {}
	for pt in pts:
		key = str(pt)
		d[key] = d.get(key, 0) + 1

	print(sum([(1 if x > 1 else 0) for x in d.values()]))

part(False)
part(True)


