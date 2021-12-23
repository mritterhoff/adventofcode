import math
from collections import defaultdict, Counter
from parse import *

f =[x for x in open("input.txt").read().strip().split('\n')]

template = f[0]
rules = dict()
for r in f[2:]:
	i, o = r.split(' -> ')
	rules[i] = [i[0] + o, o + i[1]]

D1 = defaultdict(int)
for i in range(len(template)-1):
	D1[template[i:i+2]] += 1

for s in range(1,40+1):
	D2 = defaultdict(int)
	for k,v in D1.items():
		ps = rules[k]
		D2[ps[0]] += v
		D2[ps[1]] += v
	D1=D2

count = defaultdict(int)
for k,v in D1.items():
	count[k[-1]] += v

count[template[0]] += 1
c_list = Counter(count).most_common()
print(c_list[0][1] - c_list[-1][1])

