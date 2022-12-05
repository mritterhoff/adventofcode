from parse import *

f = open("input.txt").read().strip().split('\n')

ans_p1 = 0
ans_p2 = 0
for x in f:
	r1s,r1e,r2s,r2e = parse("{:d}-{:d},{:d}-{:d}", x)
	s1 = set([x for x in range(r1s, r1e+1)])
	s2 = set([x for x in range(r2s, r2e+1)])
	if len(s1.intersection(s2)) in [len(s1), len(s2)]:
		ans_p1+=1
	if len(s1.intersection(s2))>0:
		ans_p2+=1

print('p1:', ans_p1)
print('p2:', ans_p2)