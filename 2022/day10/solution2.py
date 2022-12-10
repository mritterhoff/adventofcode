# https://adventofcode.com/2022/day/10
f = [x for x in open("input.txt").read().strip().split('\n')]

x = 1
t = 0
p1Vals = []

arr = []

def p1Work(x, t):
	t = t+1
	if t in [20,60,100,140,180,220]:
		p1Vals.append(x*t)

def checkStuff(x, t):
	p1Work(x, t)
	t = t - (t//40 * 40)
	arr.append("#" if abs(t-x) <= 1 else ' ')

for line in f:	
	if line == 'noop':
		checkStuff(x, t)	
		t+=1
	else:
		checkStuff(x, t)		
		t+=1
		
		checkStuff(x, t)
		t += 1	
		x += int(line.split(' ')[1])
	
print('p1:', sum(p1Vals))

print('p2:')
for x in range(0, 7):
	print("".join(arr[x*40:40*x+40]))
