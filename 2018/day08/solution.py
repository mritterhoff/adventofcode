import sys 
sys.path.append('../..')
from utils import *

ff = open("test.txt").read().strip()

arr = [int(x) for x in ff.split(' ')]
print(arr)

metaTotal = 0


def splitNode(arr, count):
	global metaTotal
	curCount = 0
	# lst = []
	startIndex = 0
	while curCount <= count:
		quantChildCnt = arr[startIndex]
		quantMeta = arr[startIndex+1]
		if quantChildCnt == 0:
			# lst.append((2+quantMeta))
			metaTotal += quantMeta
			startIndex += 2+quantMeta
		elif quantChildCnt == 1:
			kidContentsLen = propNode(arr[startIndex+2:])
		else:
			splitNode(arr[startIndex+2:], quantChildCnt)
		curCount+=1


# returns pair of child len and meta len
def propNode(arr):
	global metaTotal

	quantChildCnt = arr[0]
	quantMeta = arr[1]
	contents = arr[2:-quantMeta]

	if quantChildCnt == 0:
		metaTotal += quantMeta. # fix: this should sum all the quantMeta values, 
	elif quantChildCnt == 1:
		kidContentsLen = propNode(contents)
	else:
		splitNode(contents, quantChildCnt)

	return len(contents)

propNode(arr)

print(metaTotal)


































