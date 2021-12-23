import functools, operator

f = [x for x in open("input.txt").read().strip().split('\n')][0]

def hextobin(hex):
	return ''.join([bin(int(x, 16))[2:].zfill(4) for x in hex])

versions = []

def parse(bin): return parse_lit(bin) if bin[3:6] == '100' else parse_op(bin)

def parse_lit(bin):
	versions.append(int(bin[0:3], 2))
	rest = bin[6:]

	partofsub = []
	while True:
		chunk = rest[:5]
		rest = rest[5:]
		partofsub.append(chunk)
		if chunk[0] == '0': break

	return (sum([len(x) for x in partofsub]) + 6, int("".join([c[1:] for c in partofsub]), 2)), rest

def parse_op(bin):
	versions.append(int(bin[0:3], 2))
	typeID = int(bin[3:6], 2)
	ltid = bin[6]

	offset = 15 if ltid == '0' else 11
	mine = []
	rest = bin[7+offset:]
	lengthsofar = 0
	
	if ltid == '0':
		subpacketsbitlength = int(bin[7:7+offset], 2)
		while lengthsofar < subpacketsbitlength:
			popped,rest = parse(rest)
			mine.append(popped)
			lengthsofar += popped[0]
	else:
		numsubs = int(bin[7:7+offset], 2)
		while len(mine) < numsubs:
			popped,rest = parse(rest)
			mine.append(popped)
			lengthsofar += popped[0]

	return (7+offset+lengthsofar, typeID, mine), rest

def compute(packet):
	if len(packet) ==2 : return packet[1]

	cs = [compute(c) for c in packet[2]]
	if packet[1] == 0: return sum(cs)
	if packet[1] == 1: return functools.reduce(operator.mul, cs)
	if packet[1] == 2: return min(cs)
	if packet[1] == 3: return max(cs)
	if packet[1] == 5: return 1 if cs[0] > cs[1] else 0
	if packet[1] == 6: return 1 if cs[0] < cs[1] else 0
	if packet[1] == 7: return 1 if cs[0] == cs[1] else 0 

packet, rest = parse(hextobin(f))
print(f"part1 {sum(versions)}")
print(f"part2 {compute(packet)}")

