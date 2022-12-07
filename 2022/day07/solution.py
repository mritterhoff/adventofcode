from parse import *

f = [x for x in open("input.txt").read().strip().split('\n')]

# dirr is a dic with (name: name, sub: [array] contents)
# file is pair (size, name)

def execute(f, lineN, curDirObj, path):
	while(lineN and lineN < len(f)):
		rez = parse("$ {}", f[lineN])
		if rez:
			if rez[0] == 'ls':
				lineN += 1
			elif rez[0] == 'cd ..':
				return lineN + 1
			elif rez[0][0:2] == 'cd':
				rez1 = parse("cd {}", rez[0])
				dirObj = {"name": rez1[0], "sub": []}
				curDirObj['sub'].append(dirObj)
				lineN = execute(f, lineN+1, dirObj, path + dirObj['name'])
			else:
				raise
		else:
			a,b = f[lineN].split(' ')
			if a == 'dir':
				dirObj = {"name": b, "sub": []}
				curDirObj['sub'].append(dirObj)
			else:
				curDirObj['sub'].append((a, b))
			lineN += 1

root = {"name": "/", "sub": []}
execute(f, 1, root, "/")

def get_size(sizeD, curDirObj, path):
	cur_size = 0
	if curDirObj['name'] != '/': path += "/" + curDirObj['name'] 
	for sub in curDirObj['sub']:
		if type(sub) is dict:
			cur_size += get_size(sizeD, sub, path)
		else:
			cur_size += int(sub[0])
	sizeD[path] = cur_size
	return cur_size

sizeD = {}
get_size(sizeD, root, "/")
print('p1:', sum([v for k,v in sizeD.items() if v <= 100000]))

needed = 30000000 - (70000000 - sizeD['/'])
print('p2:',sorted([v for k,v in sizeD.items() if v > needed])[0])