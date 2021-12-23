import pprint
import heapq as hq
from functools import cache
from termcolor import colored
import binascii

import math
import numpy as np
import copy
from collections import defaultdict, Counter
from parse import *


f = [x for x in open("input.txt").read().strip().split('\n')][0]

def hextobin(hex):
	m = { '0': '0000',
		'1': '0001',
		'2': '0010',
		'3': '0011',
		'4': '0100',
		'5': '0101',
		'6': '0110',
		'7': '0111',
		'8': '1000',
		'9': '1001',
		'A': '1010',
		'B': '1011',
		'C': '1100',
		'D': '1101',
		'E': '1110',
		'F': '1111'}
	return ''.join([m[x] for x in hex])

versions = []

def doitall(bin):
	typeID = bin[3:6]
	packet = None
	if typeID == '100':
		packet, bin = breakup_literal(bin)		
	else:
		packet, bin = breakup_op(bin)

	# so now we have a packet (and all the packets it contains??? and the rest.)
	return (packet, bin)

def calc_length(me):
	if isinstance(me, list):
		return sum([calc_length(n) for n in me])
	else:
		return me['length']

def breakup_literal(bin):
	versions.append(int(bin[0:3], 2))
	typeID = bin[3:6]
	rest = bin[6:]

	partofsub = []
	while True:
		chunk = rest[:5]
		rest = rest[5:]
		partofsub.append(chunk)
		if chunk[0] == '0': break

	me = {
		'val': int("".join([c[1:] for c in partofsub]), 2),
		'length': sum([len(x) for x in partofsub]) + 6
	}

	return (me, rest)

def breakup_op(bin, deets={}):
	versions.append(int(bin[0:3], 2))
	typeID = bin[3:6]
	ltid = bin[6]
	if ltid == '0':
		subpacketsbitlength = int(bin[7:7+15], 2)
		rest = bin[7+15:]

		mine = []
		lengthsofar = 0
		while lengthsofar < subpacketsbitlength:
			popped,rest = doitall(rest)
			mine.append(popped)
			lengthsofar += calc_length(popped)

		me = {
			'tid':typeID,
			'length': 7+15+lengthsofar,
			'guts': mine
		}
		return (me, rest)
	else:
		numsubs = int(bin[7:7+11], 2)
		rest  = bin[7+11:]
		mine = []
		while len(mine) < numsubs:
			popped,rest = doitall(rest)
			mine.append(popped)

		me = {
			'tid':typeID,
			'length': 7+11+ calc_length(mine),
			'guts': mine
		}
		return (me, rest)

def compute(packet):
	if 'val' in packet:
		return packet['val']

	cs = [compute(c) for c in packet['guts']]
	t = int(packet['tid'], 2)
	if t == 0:
		return sum(cs)
	if t == 1:
		if len(cs) == 1:
			return cs[0]
		else:
			prod = 1
			for c in cs:
				prod *= c
			return prod
	if t == 2:
		return min(cs)
	if t == 3:
		return max(cs)
	if t == 5:
		return 1 if cs[0] > cs[1] else 0
	if t == 6:
		return 1 if cs[0] < cs[1] else 0
	if t == 7:
		return 1 if cs[0] == cs[1] else 0 
	raise 'oh no!'

def print_packet(packet):
	if 'val' in packet:
		rez  = str(packet['val'])
		# print (f"hmmmm {rez}")
		return rez

	cs = [print_packet(c) for c in packet['guts']]
	# print(cs)
	t = int(packet['tid'], 2)
	if t == 0:
		return f"sum({', '.join(cs)})"
	if t == 1:
		return f"prod({', '.join(cs)})"
	if t == 2:
		return f"min({', '.join(cs)})"
	if t == 3:
		return f"max({', '.join(cs)})"
	if t == 5:
		return f"{cs[0]} > {cs[1]}"
	if t == 6:
		return f"{cs[0]} < {cs[1]}"
	if t == 7:
		return f"{cs[0]} == {cs[1]}"
	raise 'oh no!'

packet, rest = doitall(hextobin(f))

# pprint.pp(packet)
# pprint.pp(rest)
# print("out:", print_packet(packet))

print(f"part1 {sum(versions)}")
print(f"part2 {compute(packet)}")

