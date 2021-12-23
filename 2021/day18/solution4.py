import math

class Node:
	def __init__(self, v=0, i=0, kids=[]):
		self.value = v
		self.index = i
		if len(kids) not in [0, 2]: raise 'you fucked up'
		self.l = kids[0] if len(kids) > 0 else None
		self.r = kids[1] if len(kids) > 0 else None


	def parent(self):
		return self.l and self.r

	def leaf(self):
		return not self.parent

	def __repr__(self):
		me = f'{self.value}'
		if self.parent():
			me += f" kids: {[x for x in [self.l, self.r]]}"
		return me

def newroot(c1, c2):
	return Node(0,0,[c1,c2])

a = Node(1)
b = Node(2)
print(a,b)

c = newroot(a,b)
print(c)



def magnitude(node):
	if node.parent():
		return 3*magnitude(node.l) + 2*magnitude(node.r)
	else:
		return node.value

def add(n1, n2):
	exp = newroot(n1, n2)
	renumber(exp)
	return exp

def renumber(exp, count=0):
	print(f'exp is {type(exp)}')
	if exp.parent():
		count = renumber(exp.l, count)
		count = renumber(exp.r, count)
		return count
	else:
		exp.index = count
		return count+1
	
# returns ex, remains
def qexplode(exp):
	# return ex, remains
	def get_explodee(ex, d=0):
		if ex.leaf():
			return ex, None
		if d < 3:
			lex, remains = get_explodee(ex.l, d+1)
			
			# remains mean we done
			if remains:
				ex.l = lex
				return ex, remains
			else:
				rex, remains = get_explodee(ex.r, d+1)
				if remains:
					ex.r = rex
					return ex, remains
			return ex, None
			
		else:
			if ex.l.parent():
				remains = ex.l
				ex.l = Node(0, -100)
				return ex, remains

			if ex.r.parent():
				remains = ex.r
				ex.r = Node(0, -100)
				return ex, remains
			return ex, None

	def apply_explodee(ex, remains):
		if not remains:
			return
		if ex.parent():
			apply_explodee(ex.l, remains)
			apply_explodee(ex.r, remains)
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
		if exp.leaf():
			if done:
				return exp, done
			else: 
				if exp.value > 9:
					return [Node(exp.value // 2, -100), Node(math.ceil(exp.value/2), -100)], True
				else:
					return exp, done
		else:	
			lexp, done = split(exp.l, done)
			exp.l = lexp
			rexp, done = split(exp.r, done)
			exp.r = rexp
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

def qparse(linein):
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
				return i, newroot(exp[0], exp[1])
			elif c == ',':
				pass
			else:
				raise 'oh no'
			i+=1
		print(f'exp is {str(exp)}, len is {len(exp)}')
		return i, newroot(exp[0], exp[1])

	_, exp = parse(linein)
	print(f'exp is {str(exp)}')
	renumber(exp)
	return exp

f = [x for x in open("input.txt").read().strip().split('\n')]

v = None
for exp in f:
	if v == None:
		print('meeee',exp)
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




