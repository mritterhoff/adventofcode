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

# add up all of the version numbers.

f = [x for x in open("input.txt").read().strip().split('\n')]

# def hextobin(hex):
# 	return bin(int(hex, 16))[2:]

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
	out = ""
	for x in hex:
		out += m[x]
	return out

def isop(typeId):
	return typeId != 4


vs = []


def doitall(bin):
	if len(bin) == 0:
		print('we done! rest is empty')
		return []
	if all(i in '0' for i in bin):
		print(f"done because it was {len(bin)} 0s")
		return []

	version = bin[0:3]
	typeID = bin[3:6]
	rest = bin[6:]

	# vs.append(version)
	if typeID == '100':
		return breakup_sub(bin)		
	else:
		return breakup_op(bin)



def breakup_sub(bin):
	version = bin[0:3]
	typeID = bin[3:6]
	rest = bin[6:]


	partofsub = []
	# look at the rest, 5 chars at a time
	while True:
		chunk = rest[:5]
		rest = rest[5:]
		partofsub.append(chunk)
		if chunk[0] == '0':
			break

	me = {
		# 'v':version,
		# 'tid':typeID,
		'val': int("".join([c[1:] for c in partofsub]), 2),
		'length': sum([len(x) for x in partofsub]) + 6
	}

	rez = [me]
	other = doitall(rest)
	# if isinstance(other, list):
	# 	rez.extend(other)
	# else:
	# 	rez.append(other)
	rez.extend(other)	
	return rez

def calc_length(me):
	if isinstance(me, list):
		return sum([calc_length(n) for n in me])
	else:
		return me['length']

def breakup_op(bin, deets={}):
	version = bin[0:3]
	typeID = bin[3:6]
	ltid = bin[6]
	if ltid == '0':
		lengthsubs = int(bin[7:7+15], 2)
		resetofpackets = bin[7+15:]

		subs = doitall(resetofpackets)
		mine = []
		lengthsofar = 0
		# print(f"subs are {subs}")
		# print('popping...', lengthsubs)
		while lengthsofar < lengthsubs:
			# print(f"lengthsofar {lengthsofar} lengthsubs {lengthsubs}")
			popped = subs.pop(0)
			mine.append(popped)
			lengthsofar += calc_length(popped)

		me = {
			# 'v':version,
			'tid':typeID,
			'lengthsubs': lengthsubs,
			'length': 7+15+lengthsofar,
			'guts': mine
		}
		rez = [me]
		if len(subs) > 0:
			rez.append(subs)
		return rez
	else:
		numsubs = int(bin[7:7+11], 2)
		resetofpackets  = bin[7+11:]

		# print(f"in op, ltid=1, version={version}, numsubs={numsubs}")
		# print('looking at resetofpackets', resetofpackets)
		subs = doitall(resetofpackets)

		# print(f"numsubs is {numsubs}, subs is {subs}")
		mine = subs[:numsubs]
		rest = subs[numsubs:]

		length = 7+11+ calc_length(mine)

		me = {
			# 'v':version,
			'tid':typeID,
			'numsubs': numsubs,
			'length': length,
			'guts': mine
		}
		rez = [me]
		if len(rest) > 0:
			rez.append(rest)
		return rez

# bin = hextobin('8A004A801A8002F478')
{'v': '100', 'tid': '010', 'numsubs': 1, 'guts': 
	{'v': '001', 'tid': '010', 'numsubs': 1, 'guts': 
		{'v': '101', 'tid': '010', 'lengthsubs': 11, 'guts': 
			[{'v': '110', 'tid': '100', 'guts': '1111'}]}}}

# TODO 
# so we know when a sub begins and ends, but we need to use the {deets}s to check ownership.
# or could put everything in an array, and the process it? esp if each part keeps track of it's length,
# we could then gobble up by length OR count. 


def compute(packet):
	if 'val' in packet:
		return packet['val']

	if isinstance(packet, list):
		if len(packet) == 1:
			return compute(packet[0])
		else:
			print(f"why is this a long list:")
			for p in packet:
				pprint.pp(p)

			raise 'too long!!'
			# return [compute(c) for c in packet]

	# print(f"packet {packet} ")
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
		if isinstance(cs[1], list):
			print(f"hmmm {cs[0]} anddd {cs[1]}")
		return 1 if cs[0] < cs[1] else 0
	if t == 7:
		# print(f"packet, {packet}")
		# print(f"packet['guts'], {packet['guts']}")
		# print(f"cs, {cs}")
		return 1 if cs[0] == cs[1] else 0 

	raise 'oh no!'

def print_packet(packet):
	if isinstance(packet, list):
		if len(packet) == 1:
			return print_packet(packet[0])
		else:
			# print(packet)
			return f"oh no... list of {len(packet)}"

	if 'val' in packet:
		return str(packet['val'])

	# print(f"packet {packet} ")
	cs = [print_packet(c) for c in packet['guts']]
	t = int(packet['tid'], 2)
	if t == 0:
		# return sum(cs)
		return f"sum({cs})"
	if t == 1:
		return f"prod({cs})"
	if t == 2:
		return f"min({cs})"
	if t == 3:
		return f"max({cs})"
	if t == 5:
		return f"{cs[0]} > {cs[1]}"
	if t == 6:
		if isinstance(cs[1], list):
			print(f"hmmm {cs[0]} anddd {cs[1]}")
		return f"{cs[0]} < {cs[1]}"
	if t == 7:
		# print(f"packet, {packet}")
		# print(f"packet['guts'], {packet['guts']}")
		# print(f"cs, {cs}")
		return f"{cs[0]} == {cs[1]}"

	raise 'oh no!'

f = f[0]
print(f)
bin = hextobin(f)

# bin = hextobin('9C0141080250320F1802104A08')

rez = doitall(bin)[0]
# pprint.pp(rez)
# print(print_packet(rez)[0:1000])
pprint.pp(rez)

# print("\n out:", print_packet(rez))


print('=',compute(rez))




#   File "/Users/markr/Development/personal/advent_of_code/2021/day16/solution3.py", line 227, in compute
#     return 1 if cs[0] < cs[1] else 0
# TypeError: '<' not supported between instances of 'int' and 'list'


