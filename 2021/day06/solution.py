f = [int(x) for x in open("input.txt").read().strip().split(",")]

def printy(gen,g):
	print("gen: ", g, "sum: ", sum([gen[k] for k in gen]))
	for k in sorted(gen, reverse=True): 
		print (k, gen[k])

g, nextgen = 0, {}

for x in f: nextgen[x] = nextgen.get(x,0) + 1

printy(nextgen, g)

while g < 256:
	gen = nextgen
	nextgen = {}
	for k in sorted(gen, reverse=True): 
		if k == 0:
			nextgen[6] = nextgen.get(6, 0) + gen[k]
			nextgen[8] = gen[k]
		else:
			nextgen[k-1] = gen[k]
	g+=1
	printy(nextgen, g)
