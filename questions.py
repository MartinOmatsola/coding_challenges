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
		

	
	
if __name__ == "__main__":
	#wrds = ["abc", "baa", "caan", "an", "banc"]
	#chars = ["a", "n", "c", "b"]
	#print(longestWordFromChars(wrds, chars))
	
	lst = [1 ,10, 11, 23, 4, -1, 67, 100]
	print(mergesort(lst))