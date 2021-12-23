# import pprint
# import heapq as hq
# from functools import cache
# from termcolor import colored
# import binascii



# import math
# import numpy as np
# import copy
# from collections import defaultdict, Counter
# from parse import *

# # add up all of the version numbers.

# f = [x for x in open("input.txt").read().strip().split('\n')]
# f = f[0]
# print(f)

# # def hextobin(hex):
# # 	return bin(int(hex, 16))[2:]

# def hextobin(hex):
# 	m = { '0': '0000',
# 	'1': '0001',
# 	'2': '0010',
# 	'3': '0011',
# 	'4': '0100',
# 	'5': '0101',
# 	'6': '0110',
# 	'7': '0111',
# 	'8': '1000',
# 	'9': '1001',
# 	'A': '1010',
# 	'B': '1011',
# 	'C': '1100',
# 	'D': '1101',
# 	'E': '1110',
# 	'F': '1111'}
# 	out = ""
# 	for x in hex:
# 		out += m[x]
# 	return out

# def isop(typeId):
# 	return typeId != 4


# vs = []

# def doitall(bin, deets={}):

# 	if len(bin) == 0:
# 		print('we done! rest is empty')
# 		return

# 	if all(i in '0' for i in bin):
# 		print(f"done because it was {len(bin)} 0s")
# 		return


# 	version = bin[0:3]
# 	typeID = bin[3:6]
# 	rest = bin[6:]

# 	print(f"in doitall deets={deets}, version:{version}, typeID:{typeID}, rest:{rest}")
# 	vs.append(version)
# 	if typeID == '100':
# 		return breakup_sub(bin, deets)		
# 	else:
# 		return breakup_op(bin, deets)


# def breakup_sub(bin, deets={}):
# 	# print(f"in breakup_sub with bin: {bin}")
# 	version = bin[0:3]
# 	typeID = bin[3:6]
# 	rest = bin[6:]
# 	chunks = len(rest) // 5

# 	chunks = [rest[i:i+5] for i in range(0, len(rest), 5)]	

# 	validchunkscount = 0
# 	for c in chunks:
# 		if c[0] == '1':
# 			validchunkscount+=1
# 		else:
# 			validchunkscount+=1
# 			break

# 	partofsub = chunks[0:validchunkscount]
# 	partofsub = "".join([c[1:] for c in partofsub])

# 	rest = "".join(chunks[validchunkscount:])

# 	# print('in sub, ltid=0, version', version)
# 	# print('looking at resetofpackets', rest)

# 	me = {
# 		'v':version,
# 		'tid':typeID,
# 		'guts': partofsub
# 	}

# 	return [me, doitall(rest)]


# def breakup_op(bin, exactlen=False):
# 	# print(f"in breakup_op with bin: {bin}")

# 	version = bin[0:3]
# 	typeID = bin[3:6]
# 	ltid = bin[6]
# 	if ltid == '0':
# 		length = bin[7:7+15]
# 		lengthsubs = int(length, 2)
# 		resetofpackets = bin[7+15:]

# 		subs = doitall(resetofpackets, {'lengthsubs':lengthsubs})
# 		me = {
# 			'v':version,
# 			'tid':typeID,
# 			'lengthsubs': lengthsubs,
# 			'guts': subs
# 		}
# 		return me
# 	else:
# 		length = bin[7:7+11]
# 		numsubs = int(length, 2)
# 		resetofpackets  = bin[7+11:]

# 		print(f"in op, ltid=1, version={version}, numsubs={numsubs}")
# 		print('looking at resetofpackets', resetofpackets)
# 		subs = doitall(resetofpackets, {'numsubs': numsubs})
		
# 		me = {
# 			'v':version,
# 			'tid':typeID,
# 			'numsubs': numsubs,
# 			'guts': subs
# 		}
# 		return me

# # bin = hextobin('D2FE28')
# # print(bin)
# # split = breakup(bin)
# # print(split)



# # bin = hextobin(f)

# # 011000100000000010
# #					00000000000000000101100001000101010110001011001000100000000010000100011000111000110100
# # 011000100000000010 0000000000000000010110 00010001010 10110001011 001000100000000010000100011000111000110100


# # bin = hextobin('8A004A801A8002F478')
# {'v': '100', 'tid': '010', 'numsubs': 1, 'guts': 
# 	{'v': '001', 'tid': '010', 'numsubs': 1, 'guts': 
# 		{'v': '101', 'tid': '010', 'lengthsubs': 11, 'guts': 
# 			[{'v': '110', 'tid': '100', 'guts': '1111'}]}}}

# # TODO 
# # so we know when a sub begins and ends, but we need to use the {deets}s to check ownership.
# # or could put everything in an array, and the process it? esp if each part keeps track of it's length,
# # we could then gobble up by length OR count. 

# bin = hextobin('620080001611562C8802118E34')
# {'v': '011', 'tid': '000', 'numsubs': 2, 'guts': 
# 	{'v': '000', 'tid': '000', 'lengthsubs': 22, 'guts': 
# 			[{'v': '000', 'tid': '100', 'guts': '1010'}, 
# 			[{'v': '101', 'tid': '100', 'guts': '1011'}, 
# 		{'v': '001', 'tid': '000', 'numsubs': 2, 'guts': 
# 			[{'v': '000', 'tid': '100', 'guts': '1100'}, 
# 			[{'v': '011', 'tid': '100', 'guts': '1101'}]]}]]}}


# # bin = hextobin(f)
# print(bin)
# print(doitall(bin))
#  # solution != 65


# # print(vs)
# # s = sum([int(x,2) for x in vs])
# # print('sum', s)





# # def binstrtodecnum(bin):





