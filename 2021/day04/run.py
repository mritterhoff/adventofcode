import re

class Board:
	def __init__(self, arr):
		self.arr = arr
		self.bools = []
		self.n = len(arr)
		self.col_sums = [0] * self.n
		self.row_sums = [0] * self.n
		self.finished = -1

		for row in arr:
			bools_row = []
			for el in row:
				bools_row.append(False)
			self.bools.append(bools_row)

	def num_called(self, num):
		if self.finished != -1:
			return -1
		self.mark_num(num)
		if self.is_won():
			self.finished = num
			return self.get_sum_of_unmarked()
		else: 
			return -1

	def mark_num(self, num):
		for (i,row) in enumerate(self.arr):
			for (j,value) in enumerate(row):
				if value == num:
					self.bools[i][j] = True
					self.col_sums[j] += 1
					self.row_sums[i] += 1

	def is_won(self):
		return self.n in self.row_sums or self.n in self.col_sums

	def get_sum_of_unmarked(self):
		num_sum = 0
		for (i,row) in enumerate(self.arr):
			for (j,value) in enumerate(row):
				if not self.bools[i][j]:
					num_sum += value
		return num_sum


	def __str__(self):
		return "board:\n" + '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.arr]) \
		+ "\nbools:\n" + '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.bools]) \
		+ "\n col_sums:" + str(self.col_sums) + "\n row_sums:" + str(self.row_sums)

def get_input():
	drawn = None
	boards = []
	file1 = open("input.txt")

	# split the string by one or more spaces
	# then remove any empty strings or the \n at the end
	def process_line(line):
		return [int(x) for x in re.split(r" +|\n", line) if x not in ['\n','']]

	buffer = []
	for line in file1:
		if "," in line:
			drawn = [int(x) for x in line.split(',')]

		# blank line
		elif line == '\n':
			if len(buffer) > 0:
				boards.append(buffer)
				buffer = []

		# we've got numbers
		else:
			buffer.append(process_line(line))
	# final end of file board:
	boards.append(buffer)

	return (drawn, boards)

def part_1():
	drawn, boards = get_input()

	def run_it(boards, drawn):
		bs = [Board(board) for board in boards]
		for num in drawn:
			for b in bs:
				rez = b.num_called(num)
				if rez != -1:
					return [rez, num, rez*num]

	print(run_it(boards, drawn))

def part_2():
	drawn, boards = get_input()
	bs = [Board(board) for board in boards]
	winners = []

	def run_it(bs, drawn, winners):
		for num in drawn:
			for b in bs:
				rez = b.num_called(num)
				if rez != -1:
					winners.append(b)
					# return [rez, num, rez*num]

	print(run_it(bs, drawn, winners))
	print("bslen", len(bs), 'winnerslen', len(winners))

	last = winners[-1]
	rez = last.get_sum_of_unmarked()
	num = last.finished
	print([rez, num, rez*num])

part_2()





