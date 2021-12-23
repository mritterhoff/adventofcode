def part_1():
	file1 = open("input.txt")

	input = []
	counter = {}

	for line in file1:
		input.append(line)
		print(line)
		for i in range(0, len(line)-1):
			counter[i] = counter.get(i, 0) + (1 if line[i] == "1" else 0)


	print(counter)
	print(len(input))


	gamma = ""
	epsilon = ""

	for i in range(0, len(input[0])-1):
		gamma += "0" if counter[i] < 500 else "1"
		epsilon += "1" if counter[i] <= 500 else "0"
	print(gamma)
	print(epsilon)
	print(int(gamma, 2)*int(epsilon, 2))

def part_2():
	def getinput():
		file1 = open("input.txt")
		input = []
		for line in file1:
			input.append(line)
		return input
		# return [
		# "00100",
		# "11110",
		# "10110",
		# "10111",
		# "10101",
		# "01111",
		# "00111",
		# "11100",
		# "10000",
		# "11001",
		# "00010",
		# "01010"]

	def calculate(inski):
		counter = {}
		for line in inski:
			for i in range(0, len(line)):
				counter[i] = counter.get(i, 0) + (1 if line[i] == "1" else 0)

		gamma = ""
		epsilon = ""

		for i in range(0, len(inski[0])):
			gamma += "0" if counter[i] < len(inski)/2 else "1"
			epsilon += "1" if counter[i] < len(inski)/2 else "0"

		print(counter)
		print(len(inski))
		print(["gamma", gamma, "episilon", epsilon])
		return [gamma, epsilon]

	input = getinput()
	print("input", input)

	bin_len = len(input[0]) + 1

	pattern = ""
	ox = ""
	
	for i in range(0, bin_len):
		output = []
		pattern = calculate(input)[0][0:i+1]
		print("trying: {}...".format(pattern))
		for el in input:
			if el.startswith(pattern):
				output.append(el)
		print(["i", i, "result count", len(output)])
		if len(output) == 1:
			ox = output
			break
		input = output

	print("output:")
	print([pattern, ox])


	pattern = ""
	co = ""
	input = getinput()
	for i in range(0, bin_len):
		output = []
		pattern = calculate(input)[1][0:i+1]
		for el in input:
			if el.startswith(pattern[i], i):
				output.append(el)
		if len(output) <= 1:
			co = output
			break
		input = output

	print(int(ox[0], 2)*int(co[0], 2))

	# 7108703 is too high
	# 7108703
	# 7041258

part_2()