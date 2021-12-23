import math

class Node:
	def __init__(self, v=0, i=0):
		self.value = v
		self.index = i

def magnitude(exp):
	if isinstance(exp, list):
		return 3*magnitude(exp[0]) + 2*magnitude(exp[1])
	else:
		return exp.value

def add(x1, x2):
	exp = [x1, x2]
	renumber(exp)  # FUUUUUUUU (this was the last missing piece)
	return exp

def renumber(exp, count=0):
	if isinstance(exp, list):
		count = renumber(exp[0], count)
		count = renumber(exp[1], count)
		return count
	else:
		exp.index = count
		return count+1
	
# returns ex, remains
def qexplode(exp):
	# return ex, remains
	def get_explodee(ex, d=0):
		if isinstance(ex, Node):
			return ex, None
		if d < 3:
			lex, remains = get_explodee(ex[0], d+1)
			
			# remains mean we done
			if remains:
				ex[0] = lex
				return ex, remains
			else:
				rex, remains = get_explodee(ex[1], d+1)
				if remains:
					ex[1] = rex
					return ex, remains
			return ex, None
			
		else:
			if isinstance(ex[0], list):
				remains = ex[0]
				ex[0] = Node(0, -100)
				return ex, remains

			if isinstance(ex[1], list):
				remains = ex[1]
				ex[1] = Node(0, -100)
				return ex, remains
			return ex, None

	def apply_explodee(ex, remains):
		if not remains:
			return
		if isinstance(ex, list):
			apply_explodee(ex[0], remains)
			apply_explodee(ex[1], remains)
		else:
			if ex.index == remains[0].index - 1:
				ex.value += remains[0].value
			elif ex.index == remains[1].index + 1: 
				ex.value += remains[1].value

	exp, remains = get_explodee(exp)
	apply_explodee(exp, remains)
	renumber(exp)
	return exp, remains

def qsplit(exp):
	# returns exp, done
	def split(exp, done = False):
		if isinstance(exp, Node):
			if done:
				return exp, done
			else: 
				if exp.value > 9:
					return [Node(exp.value // 2, -100), Node(math.ceil(exp.value/2), -100)], True
				else:
					return exp, done
		else:	
			lexp, done = split(exp[0], done)
			exp[0] = lexp
			rexp, done = split(exp[1], done)
			exp[1] = rexp
			return exp, done

	exp, splitted = split(exp)
	renumber(exp)
	return exp, splitted

# returns exp
def reduce(exp):
	exploded = True
	
	# if you exploded once, try again:
	while exploded:
		exp, exploded = qexplode(exp)

	exp, splitted = qsplit(exp)

	if splitted:
		exp = reduce(exp)
	return exp

def qparse(exp):
	def parse(line, i=0):
		L = len(line)
		exp = []
		while i < L:
			c = line[i]
			if '0' <= c <= '9':
				exp.append(Node(int(c)))
			elif c == '[':
				i, exp_n = parse(line, i+1)
				exp.append(exp_n)
			elif c == ']':
				return i, exp
			elif c == ',':
				pass
			else:
				raise 'oh no'
			i+=1
		return i, exp

	_, exp = parse(exp)
	exp = exp[0]
	renumber(exp)
	return exp

f = [x for x in open("input.txt").read().strip().split('\n')]

v = None
for exp in f:
	if v == None:
		v = qparse(exp)
	else:
		v = reduce(add(v, qparse(exp)))
print('part1', magnitude(v))

# out = []
# for i in range(len(f)):
# 	for j in range(len(f)):
# 		if i!=j:
# 			out.append(magnitude(reduce(add(qparse(f[i]), qparse(f[j])))))
# print('part2', max(out))




