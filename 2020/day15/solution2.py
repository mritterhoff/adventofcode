from collections import defaultdict

f = [int(x) for x in open("input.txt").read().strip().split(',')]


print(f)

# number spoken to list of turns (TODO cap list length at 2)
D = defaultdict(list)

last = None
turn = 1
for x in f:
	last = x
	D[x].append(turn)
	turn+=1
print('last is ', last)
print('turn is', turn)
print('D is', D)

for t in range(len(f)+1, 30000000+1):
	if t % 100000 == 0: print(t)
	# we've said last before
	if last in D:
		turns_last_spoken = D[last]
		if len(turns_last_spoken) == 1:
			D[0].append(t)
			last = 0
		else:
			last = turns_last_spoken[-1] - turns_last_spoken[-2] 
			D[last].append(t)
	else:
		D[0].append(t)
		last = 0
	# print(t, last, D)

print(last)


# kinda slow, but works.