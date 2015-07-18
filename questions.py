import sys

def longestWordFromChars(wrds, chars):
	charMap = {}
	for char in chars:
		if charMap.has_key(char):
			charMap[char] += 1
		else:
			charMap[char] = 1
		
	longestWords = {}
	maxLen = 0
	for wrd in wrds:
		areAllCharsInCharMap = True
		localMap = charMap.copy()
		for c in wrd:
			if localMap.has_key(c) and localMap[c] > 0:
				localMap[c] -= 1
			else:
				areAllCharsInCharMap = False
				break
		
		if areAllCharsInCharMap:
			strLength = len(wrd)
			if not longestWords.has_key(strLength):
				longestWords[strLength] = []
			longestWords[strLength].append(wrd)
			if strLength >= maxLen:
				maxLen = strLength
	
	if longestWords.has_key(maxLen):
		return longestWords[maxLen]
	
	return []
	
def mergesort(lst):
	def merge(lst1, lst2):
		return mergehelper(lst1, lst2, [])
		
	def mergehelper(lst1, lst2, acc):
		if (len(lst1) == 0) and len(lst2) > 0:
			for x in lst2:
				acc.append(x)
			return acc
		
		if (len(lst2) == 0) and len(lst1) > 0:
			for x in lst1:
				acc.append(x)
			return acc
		
		if lst1[0] <= lst2[0]:
			v = lst1[0]
			acc.append(v)
			return mergehelper(lst1[1:], lst2, acc)
		else:
			v = lst2[0]
			acc.append(v)
			return mergehelper(lst1, lst2[1:], acc)
	
	if len(lst) > 1:
		mid = len(lst)/2
		return merge(mergesort(lst[0:mid]), mergesort(lst[mid:]))
	else:
		return lst
		
def addUpTo100(lst):
	map = {}
	for i in lst:
		if map.has_key(i):
			map[i] += 1
		else:
			map[i] = 1
		
	ret = []
	for k in lst:
		if k == 50: 
			if map[50] > 1:
				ret.append((50, 50))
				map[50] -= 2
		elif map.has_key(100 - k) and map[100 - k] > 0 and map[k] > 0:
			ret.append((k, 100 - k))
			map[k] -= 1
			map[100 - k] -= 1
	return ret
	
def printInStringOrder(ubound):
	def inner(pfx, ubound):
		if int(pfx) > ubound: return
		for i in range(10):
			s = pfx + str(i)
			if int(s) <= ubound:
				sys.stdout.write(s + ", ")
				inner(s, ubound)
			
	for i in range(1, 10):
		sys.stdout.write(str(i) + ", ")
		inner(str(i), ubound)
		
def getLongestCommonPrefix(s1, s2):
	n = len(s2)
	pfx = ""
	while n >= 0:
		pfx = s2[0:n]
		if pfx == s1[0:n]: break
		n -= 1
	return pfx
	
def getLongestCommonPrefixInSentence(s):
	words = sorted(s.split(" "))
	candidate = words[0]
	for i in range(1, len(words)):
		candidate = getLongestCommonPrefix(words[i], candidate)
	return candidate

def lehmerRandomNumber(seed, a, c, m):
	yield seed
	while True:
		num = ((a * seed) + c) % m
		yield num
		seed = num

def bucket_sort(arr, upper_bound):
	bucket = [0] * (upper_bound + 1)
	for i in arr:
		bucket[i] += 1

	sorted_arr = []
	for i in xrange(0, upper_bound + 1):
		for j in xrange(bucket[i]):
			sorted_arr.append(i)

	return sorted_arr

def atoi(chars):
	chars = list(chars)
	count = len(chars)
	i = count - 1

	acc = 0
	while i >= 0: 
		acc += (ord(chars[i]) - ord('0')) * (10 ** (count - i - 1))
		i -= 1

	return acc

def nWayMerge(arr):
	"""
	Merge a list on n sorted lists into a single sorted list
	"""

	numLists = len(arr)
	curIndexes = [0] * numLists
	output = []

	done = False
	while not done:
		done = True
		minimum = (sys.maxint, -1)

		for i in xrange(0, numLists):
			if curIndexes[i] < len(arr[i]):
				done = False
				curElem = arr[i][curIndexes[i]]
				if curElem <= minimum[0]:
					minimum = (curElem, i)

		if minimum[1] != -1:
			output.append(minimum[0])
			curIndexes[minimum[1]] += 1

	return output
	
	
if __name__ == "__main__":

	sortedLists = [
		[1, 2, 3, 4, 5],
		[6, 7, 8, 8, 9, 10],
		[11, 12, 13, 14, 15, 16, 16]
	]

	print nWayMerge(sortedLists)


	# arr = [4 , 0 , 2, 10, 0, 4, 3]
	# sorted_arr = bucket_sort(arr, 10)
	# print sorted_arr


	#wrds = ["abc", "baa", "caan", "an", "banc"]
	#chars = ["a", "n", "c", "b"]
	#print(longestWordFromChars(wrds, chars))
	
	#lst = [1 ,10, 11, 23, 4, -1, 67, 100, 0, 25, 75, -1, 101, 50, 50, 50]
	#print(mergesort(lst))
	
	#print addUpTo100(lst)
	
	#printInStringOrder(1000)
	
	#print getLongestCommonPrefixInSentence("abcd abcdef abcdxxx abcdeee")

	# count = 0
	# for i in lehmerRandomNumber(0, 13, 1, 16):
	# 	print i
	# 	count += 1
	# 	if count > 5: 
	# 		break
	# 