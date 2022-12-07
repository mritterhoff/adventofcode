from utils import *

# multiple lines
f = [x for x in open("input.txt").read().strip().split('\n')]


# total size of each directory

# dirr is a dic with (name: name, contents: [array] contents)
# file is pair (size, name)

def getFile(cur_dirr, name):
	for a in cur_dirr['sub']:
		if type(a) is tuple:
			if a[1] == name:
				return a
	return None

def getDir(cur_dirr, name):
	for a in cur_dirr['sub']:
		if type(a) is dict:
			if a['name'] == name:
				return a
	return None

lines = []
all_dirs = set()
all_files = set()

root = {"name": "/", "sub": []}

def execute(f, lineN, cur_dirr, path):
	curc = ""
	while(lineN and lineN < len(f)):
		# print('lineN:', lineN)
		# print(f[lineN])
		lines.append(lineN)
		rez = parse("$ {}",f[lineN])
		if rez:
			if rez[0] == 'ls':
				curc = 'ls'
				lineN += 1
			elif rez[0] == 'cd ..':
				return lineN + 1
			elif rez[0][0:2] == 'cd':
				rez1 = parse("cd {}", rez[0])
				# print('new_dirr_name', new_dirr_name[0] )
				dirpoint = getDir(cur_dirr, rez1[0])
				if not dirpoint: 
					dirpoint = {"name": new_dirr_name, "sub": []}
					cur_dirr['sub'].append(dirpoint)
					if path + new_dirr_name in all_dirs:
						print(path + new_dirr_name)
						raise 'duplicate dir'
					all_dirs.add(path + new_dirr_name)
				lineN = execute(f, lineN+1, dirpoint, path + dirpoint['name'])
			else:
				print('error, unexpected!', lineN, f[lineN])
				raise
		else:
			if curc == 'ls':
				a,b = f[lineN].split(' ')
				# print('a,b', a, b)
				if a == 'dir':
					if not getDir(cur_dirr, b):
						dirpoint = {"name": b, "sub": []}
						cur_dirr['sub'].append(dirpoint)
						if path + b in all_dirs:
							print(path + b)
							raise 'duplicate dir'
						all_dirs.add(path + b)
				else:
					print(a,b)
					file_point = getFile(cur_dirr, b)
					if b == 'bch.lht':
						print("cur_dirr", cur_dirr)
					if file_point:
						file_point[0] = a
					else:
						cur_dirr['sub'].append((a, b))
						# if b in all_files:
						# 	print(b)
						# 	raise 'duplicate file'
						all_files.add(b)

				lineN += 1


execute(f, 1, root, "/")

pp(root)

# pp(lines)

def get_size(sizeD, cur_dirr, path):
	cur_size = 0
	path = path + "/" + cur_dirr['name'] 
	for sub in cur_dirr['sub']:
		if type(sub) is dict:
			size = get_size(sizeD, sub, path)
			cur_size += size

		else:
			cur_size += int(sub[0])
	# print('cur_dirr:', cur_dirr)		
	# print('cur_dirr[name]:', cur_dirr['name'])
	sizeD[path] = cur_size
	return cur_size
	

sizeD = {}
get_size(sizeD, root, "")
pp(sizeD)

s = 0
for k,y in sizeD.items():
	if y <= 100000:
	   s += y
# print(s)

# for x in range(len(f)):
# 	if x not in lines:
# 		print(x,' was missing!!!')


# 921955 is not the right answer


# get items in sorted order by keys, largest to smallest
s = sorted(sizeD.items(), key=lambda x: x[1], reverse=True)

cur_free = 70000000 - 47048086
needed = 30000000 - cur_free

out = []
for k,v in sizeD.items():
	if v > needed:
		out.append(v)

print(sorted(out))



# 304195 is too low

# 37948890 is too high


































