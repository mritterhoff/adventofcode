import math

f =[x for x in open("input.txt").read().strip().split('\n')]
f = np.asarray([[int(y) for y in x] for x in f])
print(f)

R = len(f)
C = len(f[0])

def do_flash(fnew, x, y):
	fnew[y][x] += 1
	for xd in [-1, 0, 1]:
		for yd in [-1, 0, 1]:
			iy = y + yd
			ix = x + xd
			if 0 <= iy < R and 0 <= ix < C and (iy,ix) != (y,x):
				if fnew[iy][ix] != 10:
					fnew[iy][ix] = fnew[iy][ix] + 1
					if fnew[iy][ix] == 10:
						do_flash(fnew,ix,iy)

flashes = 0
rez = [f]
for gen in range(0, 1000):
	print('it gen:', gen+1)
	fold = rez[-1]
	fnew = np.empty([C,R], dtype=int)
	for iy in range(R):
		for ix in range(C):
			fnew[iy][ix] = fold[iy][ix] + 1

	f_gen = 0
	for iy in range(R):
		for ix in range(C):
			if fnew[iy][ix] == 10:
				do_flash(fnew,ix,iy)

	for iy in range(R):
		for ix in range(C):
			if fnew[iy][ix] > 9:
				fnew[iy][ix] = 0
				flashes += 1
						
	if np.all(fnew == 0):
		print(fnew)
		print('done', gen)
		break

	rez.append(fnew)
	# print(fnew)
	# print(flashes)
