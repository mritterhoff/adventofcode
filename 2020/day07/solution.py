import re

def part_1():
	f = [x for x in open("input.txt").read().strip().split('\n')]
	f = [x.split(' bags contain ') for x in f]
	m = {}
	for l in f:
		color = l.pop(0)
		cc = [x.strip(' .') for x in l[0].split(',')]
		count_color_pairs = [re.match('(\d+) (.*) bags?', x).groups() for x in cc if x != 'no other bags']

		# ignore count for now
		# print(color, [x[1] for x in count_color_pairs])
		m[color] = [x[1] for x in count_color_pairs]

	print(m)

	def get_to_gold(color, m):
		# print(color, m)
		colors = m[color]
		if len(colors) == 0:
			return False

		if 'shiny gold' in colors:
			return True

		for color in colors:
			if get_to_gold(color, m):
				return True

		return False

	count = 0
	for color in m.keys():
		if get_to_gold(color, m):
			count += 1

	print(count)

def part_2():
	f = [x for x in open("test.txt").read().strip().split('\n')]
	f = [x.split(' bags contain ') for x in f]
	m = {}
	for l in f:
		color = l.pop(0)
		cc = [x.strip(' .') for x in l[0].split(',')]
		count_color_pairs = [re.match('(\d+) (.*) bags?', x).groups() for x in cc if x != 'no other bags']

		# ignore count for now
		# print(color, [x[1] for x in count_color_pairs])
		m[color] = [(int(x[0]), x[1]) for x in count_color_pairs]

	print(m)

	def get_to_gold(count_color_pair, m):
		print(count_color_pair)
		count, color = count_color_pair

		count_color_pairs = m[color]
		if len(count_color_pairs) == 0:
			print(color, 'has no more bags')
			return 1

		contains_bags = sum([next_pair[0]*get_to_gold(next_pair, m) for next_pair in count_color_pairs]) + 1
		print(color, "gets", count, "times", contains_bags, "that is:", count_color_pairs)
		return count * contains_bags

	print(get_to_gold((1, 'shiny gold'), m))

# part_2()

def part_2b():
	f = [x for x in open("input.txt").read().strip().split('\n')]
	f = [x.split(' bags contain ') for x in f]
	m = {}
	for l in f:
		color = l.pop(0)
		cc = [x.strip(' .') for x in l[0].split(',')]
		count_color_pairs = [re.match('(\d+) (.*) bags?', x).groups() for x in cc if x != 'no other bags']

		# ignore count for now
		# print(color, [x[1] for x in count_color_pairs])
		m[color] = [(int(x[0]), x[1]) for x in count_color_pairs]

	print(m)

	def bags_in_me(color, m):
		print(color, 'has...')

		mappings = m[color]

		if len(mappings) == 0:
			rez = 0
		else:
			rez = sum([count*(bags_in_me(color, m)+1) for count, color in mappings])

		return rez


	# def get_to_gold(count_color_pair, m):
	# 	print(count_color_pair)
	# 	count, color = count_color_pair

	# 	count_color_pairs = m[color]
	# 	if len(count_color_pairs) == 0:
	# 		print(color, 'has no more bags')
	# 		return 1

	# 	contains_bags = sum([next_pair[0]*get_to_gold(next_pair, m) for next_pair in count_color_pairs]) + 1
	# 	print(color, "gets", count, "times", contains_bags, "that is:", count_color_pairs)
	# 	return count * contains_bags

	print(bags_in_me('shiny gold', m))

part_2b()



