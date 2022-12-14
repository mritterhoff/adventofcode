import sys 
sys.path.append('../..')
from utils import *

import sys
sys.setrecursionlimit(100000)

ff = open("test.txt").read().strip()

arr = [int(x) for x in ff.split(' ')]
print(arr)

metaTotal = 0


# def splitNode(arr, count):
# 	global metaTotal
# 	curCount = 0
# 	# lst = []
# 	startIndex = 0
# 	while curCount <= count:
# 		quantChildCnt = arr[startIndex]
# 		quantMeta = arr[startIndex+1]
# 		if quantChildCnt == 0:
# 			# lst.append((2+quantMeta))
# 			metaTotal += quantMeta
# 			startIndex += 2+quantMeta
# 		elif quantChildCnt == 1:
# 			kidContentsLen = propNode(arr[startIndex+2:])
# 		else:
# 			splitNode(arr[startIndex+2:], quantChildCnt)
# 		curCount+=1


# do we return start and end,
# or just our full length?
def propNode(arr, start, end, depth):
	global metaTotal
	# if depth > 10:
	# 	return

	quantChildCnt = arr[start]
	quantMeta = arr[start+1]

	print(start, end, quantChildCnt)

	# if depth == 0:
	# 	end = end-quantMeta
	# 	print('meta is:', arr[-quantMeta:])
	# 	metaTotal += sum(arr[-quantMeta:])

	if quantChildCnt == 0:
		print('meta is:', arr[start+2:start+2+quantMeta])
		metaTotal += sum(arr[start+2:start+2+quantMeta])
		print('my length is', 2+quantMeta)

		return 2+quantMeta
	elif quantChildCnt == 1:
		childLen = propNode(arr, start+2, end, depth+1)
		
		print('meta is:', arr[start+2+childLen:start+2+childLen+quantMeta])
		metaTotal += sum(arr[start+2+childLen:start+2+childLen+quantMeta])
		print('my length is', 2 + childLen + quantMeta)
		
		return 2 + childLen + quantMeta
	else:
		childrenLength = 0
		while childrenLength < (end - start - 2 - quantMeta):
			childrenLength += propNode(arr, start+2+childrenLength, end, depth+1)
		
		print('meta is:', arr[start+2+childrenLength:start+2+childrenLength+quantMeta])
		metaTotal += sum(arr[start+2+childrenLength:start+2+childrenLength+quantMeta])
		print('my length is', 2 + childrenLength + quantMeta)
		
		return 2 + childrenLength + quantMeta

propNode(arr, 0, len(arr)-1, 0)

print(metaTotal)



# 28476 is too low






























