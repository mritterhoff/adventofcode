import math

f = [x for x in open("input.txt").read().strip().split('\n')]

r=[]
for row in f:
	p=[]
	for el in row:
		p.append(int(el))
	r.append(p)
f = r

def out(f,x,y):
	xmax = len(f[0])
	ymax = len(f)

	left = x-1
	right = x+1
	up = y+1
	down=y-1

	if left>=0 and f[y][left] <= f[y][x]:
		return -1
	elif right<xmax and f[y][right] <= f[y][x]:
		return -1
	elif down>=0 and f[down][x] <= f[y][x]:	
		return -1
	elif up<ymax and f[up][x] <= f[y][x]:	
		return -1
	return f[y][x]
				
def part1():
	rez = []
	for iy, row in enumerate(f):
		for ix, el in enumerate(row):
			o = out(f,ix,iy)
			if o != -1:
				rez.append(o)

	print(rez)
	print(sum([x+1 for x in rez]))


def non9neighbors(f,x,y):
	xmax = len(f[0])
	ymax = len(f)

	left = x-1
	right = x+1
	up = y+1
	down=y-1

	rez = []
	if left>=0 and f[y][left] not in [9, -1]:
		rez.append((left,y))
	if right<xmax and f[y][right] not in [9, -1]:
		rez.append((right,y))
	if down>=0 and f[down][x] not in [9, -1]:
		rez.append((x, down))
	if up<ymax and f[up][x] not in [9, -1]:
		rez.append((x, up))
	
	return rez

def fill(f,x,y):
	if f[y][x] in [-1, 9]: return 0

	f[y][x] = -1

	return sum([fill(f,p[0], p[1]) for p in non9neighbors(f,x,y)]) + 1

print(f)

rez = []
for iy, row in enumerate(f):
	for ix, el in enumerate(row):
		if f[iy][ix] not in [-1, 9]:
			r = fill(f,ix,iy)
			if r > 0:
				rez.append(r)

print(sorted(rez)[-3:])

mult = 1
for x in sorted(rez)[-3:]:
	mult *= x
print(mult)






