import copy
import pprint
f = [x for x in open("input.txt").read().strip().split('\n')]

print(f)

D = dict()

z = 0
R = len(f)
C = len(f[0])
for r in range(R):  # y
	for c in range(C): # x
		D[(c,r,z,0)] = f[r][c] == '#'

# can cache this
def getneighbors(tup_in):
	x,y,z,w = tup_in
	neighbors = []
	for dx in [-1,0,1]:
		for dy in [-1,0,1]:
			for dz in [-1,0,1]:
				for dw in [-1,0,1]:
					poss = (x+dx, y+dy, z+dz, w+dw)
					if tup_in != poss:
						neighbors.append(poss)
	return neighbors

def neighborson(D, ns):
	count = 0
	for n in ns:
		if n in D:
			count += 1 if D[n] else 0
		else:
			D[n] = False
	return count

# If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. 
# 	Otherwise, the cube becomes inactive.
# If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. 
# 	Otherwise, the cube remains inactive.
def amion(D, pt, state):
	n_on = neighborson(D, getneighbors(pt))
	if state:
		return n_on in [2,3]
	else:
		return n_on == 3


def getalldimen(D, dimen_i):
	l = [d[dimen_i] for d in D.keys()]
	return (min(l), max(l))

def print_me(D1):
	return
	# xmin, xmax = getalldimen(D1,0)
	# ymin, ymax = getalldimen(D1,1)
	# zmin, zmax = getalldimen(D1,2)
	# wmin, wmax = getalldimen(D1,3)
	# for z in range(zmin,zmax+1):
	# 	zout = ""
	# 	for y in range(ymin,ymax+1):
	# 		yout=[]
	# 		for x in range(xmin,xmax+1):
	# 			yout.append('#' if D1[(x,y,z)] else '.')
	# 		zout += "".join(yout)
	# 		zout += "\n"
	# 	print('z:', z)
	# 	# pprint.pp(zout)
	# 	print(zout)



D1 = D
for gen in range(1, 6+1):
	print('gen, len D', gen, len(D1))
	D2 = dict()
	xmin, xmax = getalldimen(D1,0)
	ymin, ymax = getalldimen(D1,1)
	zmin, zmax = getalldimen(D1,2)
	wmin, wmax = getalldimen(D1,3)
	print(xmin, xmax, ymin, ymax, zmin, zmax, wmin, wmax)

	for x in range(xmin-1,xmax+2):
		for y in range(ymin-1,ymax+2):
			for z in range(zmin-1,zmax+2):
				for w in range(wmin-1,wmax+2):
					pt = (x,y,z,w)
					inital_state = False
					if pt in D1:
						inital_state = D1[pt]
					D2[pt] = amion(D1, pt, inital_state)
	
	print('gen:', gen)
	print_me(D2)
	print(sum([x for x in D2.values()]))
	D1 = copy.deepcopy(D2)

# xmin, xmax = getalldimen(D1,0)
# ymin, ymax = getalldimen(D1,1)
# zmin, zmax = getalldimen(D1,2)


# print(sum([x for x in D1.values()]))