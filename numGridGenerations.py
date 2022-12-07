from utils import *

f =[x for x in open("sample_input/number_grid.txt").read().strip().split('\n')]
state = np.asarray([[int(el) for el in row] for row in f])
print(state)

R,C = state.shape
print('rows:', R, ' cols:', C)

hist = [state]
for gen in range(0, 2):
	print('gen:', gen+1)
	old = hist[-1]
	new = np.full((R,C), 0)

	for iy in range(R):
		for ix in range(C):
			 for pt in ns_8((ix, iy), R, C):
		 	pp(pt)

	hist.append(new)
	pp(old)
	pp(new)
