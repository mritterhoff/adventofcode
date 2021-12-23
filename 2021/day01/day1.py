# 1532
def part_1():
	lst = [int(x) for x in open("input.txt").read().strip().split()]

	count=0
	for idx, val in enumerate(lst):
		if idx>0 and val>lst[idx-1]:
			count +=1

	print(count)

	# best way
	print(len([(x,y) for x,y in list(zip(lst[:-1], lst[1:])) if x < y]))

def part_2():
	file1 = open("input.txt")
	arr = [0, 0, 0]
	count = 0

	for line in file1:
	
		# if len(arr) > 20:
		# 	break

		print(arr[-3:])
		old = sum(arr[-3:])
		arr.append(int(line))
		new = sum(arr[-3:])
		print([old, new, "increased!" if new > old else ""])

		if new > old:
			count += 1

	print(count) - 3


part_1()