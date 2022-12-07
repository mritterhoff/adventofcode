from utils import *

f =[x for x in open("sample_input/number_grid.txt").read().strip().split('\n')]

og = np.asarray([[int(el) for el in row] for row in f])

def printArr(arr):
	for row in arr: print(row)


def tileArray(arr, horiz, vert, permuteLambda = lambda aIn,h,v: aIn):
	out = []	
	for v in range(vert):		
		for h in range(horiz):
			newTile = permuteLambda(arr, h, v)
			if h == 0: newArrayRow = newTile
			else: newArrayRow = np.concatenate((newArrayRow, newTile), axis=1)
		if v == 0: out = newArrayRow
		else: out = np.concatenate((out, newArrayRow), axis=0)
	return out

	
def lammy(aIn,h,v):
	out = np.full(aIn.shape, 0)
	for r in range(aIn.shape[0]):
		for c in range(aIn.shape[1]):
			out[r][c] = (h+v)*10 + aIn[r][c]
	return out 

printArr(tileArray(og, 5, 5, lammy))

