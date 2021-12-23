f = [int(x) for x in open("test.txt").read().strip().split(',')]

# def is_first(n):
# 	return 1==len([x for x in f if x==n])

def second_most_recent_i(n):
	rez = -1
	for i in range(len(f)-1):
		if f[i] == n:
			rez = i
	return rez
			

# orig_l = len(f)
# for t in range(1,2020):
# 	if t < orig_l:
# 		continue
# 	last_f = f[-1]
# 	if is_first(last_f):
# 		f.append(0)
# 	else:
# 		n = len(f)-1 - second_most_recent_i(last_f)
# 		f.append(n)

# print(f[-1])


# keep a dict, and with it the last 2 indicies of a number,
dict = {}
def add(k,v):
	if k in dict:
		oldv = dict[k]
		if len(oldv) == 2:
			r = oldv.pop(0)
			oldv.append(v)
		else:
			oldv.append(v)
	else:
		dict[k] = [v]
	return dict[k]



orig_l = len(f)
for t in range(0,10):
	if t < orig_l -1 :
		add(f[t], t)
		print(t, f, dict)
		continue
	last_spoken = f[t-1]

	if last_spoken in dict:
		arr = dict[last_spoken]
		## if equal to 1, just add 0 to f	
		if len(arr) == 1:
			f.append(0)
			add(last_spoken, t-1)
		else:
			arr = add(last_spoken, t-1)
			n = t-1 - arr[0]
			f.append(n)
	else:
		add(last_spoken, t-1)
	print(t, f, dict)

# print(f)