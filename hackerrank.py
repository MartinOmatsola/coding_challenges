import itertools, sys, math

def isPalindrome(s):
    return s == s[::-1]

def getNumEdits(s):
	if isPalindrome(s): return 0

	strLength = len(s)
	mid = int(strLength/2)
	
	numEdits = 0
	currentCharIndex = strLength - 1
	while currentCharIndex >= mid:
		if s[currentCharIndex] != (s[strLength - currentCharIndex - 1]):
			numEdits += abs(ord(s[currentCharIndex]) - ord(s[strLength - currentCharIndex - 1]))
			if ord(s[strLength - currentCharIndex - 1]) <= ord(s[currentCharIndex]):
				s[currentCharIndex] = s[strLength - currentCharIndex - 1]
			else:
				s[strLength - currentCharIndex - 1] = s[currentCharIndex]
				
		if isPalindrome("".join(s)): break
		currentCharIndex -= 1
	
	return numEdits

def getIntersect(str1, str2):
	return set(str1).intersection(set(str2))
	
def permutation(s):
	def permute(pfx, s2, acc=None):
		if acc is None:
			acc = set()
	
		n = len(s2)
		acc.add(pfx)
		
		if n == 0:
			return acc
		else:
			for i in range(n):
				return permute(pfx + s2[i], s2[0:i] + s2[i+1:], acc)
	
	
	return permute('', s)

def canBePalindrome(s):
	isEven = (len(s) % 2) == 0

	hash = {}
	for c in s:
		if not hash.has_key(c):
			hash[c] = 0
		hash[c] += 1

	flag = True
	oneCount = evenCount = oddCount = 0
	numKeys = len(hash.keys())

	for k,v in hash.iteritems():
		isValEven = (v % 2) == 0
		if isValEven:
			evenCount += 1
		else:
			oddCount += 1


	if isEven and oddCount == 0:
		return True

	if not isEven and oddCount == 1:
		return True

	return False

def maxXor(l, r):
	nums = list(range(l, r+1))

	even = [x for x in nums if x % 2 == 0]
	odd = [x for x in nums if x % 2 == 1]

	myMax = 0
	for i in even:
		for j in odd:
			val = i ^ j
			if val > myMax:
				myMax = val
	
	return myMax

def findDigits(num):
	tmp = str(num)
	ret = 0
	for i in tmp:
		#print i
		n = int(i)
		if n == 0: continue
		if num % n == 0: ret += 1

	return ret

def isDecent(num):
	tmp = str(num)
	count3 = 0
	count5 = 0
	for i in tmp:
		if not i in ['3', '5']: return False
		if i == '3': count3 += 1
		elif i == '5': count5 += 1
	
	if (count3 % 5 == 0) and (count5 % 3 == 0):
		return True

	return False

def sherlockAndBeast(n):
	numStr = n * '5'
	numInt = int(numStr)

	count5 = n
	count3 = 0

	if count5 % 3 == 0: return numInt
	
	numList = list(numStr)
	count = len(numList)
	for i in range(count):
		numList[count - i - 1] = '3'
		count3 += 1
		count5 -= 1
		num = int(''.join(numList))
		if (count5 % 3 == 0) and (count3 % 5 == 0): return num

	return -1

#print isDecent(55555533333)

def gcdList(lst):
	from fractions import gcd

	count = len(lst)
	ret = lst[0]
	for i in range(1, count):
		ret = gcd(ret, lst[i])

	return ret == 1

def angryChildren(n, k, candies):
	minDiff = candies[n-1]

	for i in range(n-k):
		#tmp = candies[i:i+k]
		#print tmp
		#x = max(tmp) - min(tmp)

		x = candies[i+k-1] - candies[i]
		if x < minDiff:
			minDiff = x

	return minDiff

def fibo(n):
	if n == 0: return 0
	if n == 1: return 1

	prev1 = 0
	prev2 = 1
	for i in xrange(1, n):
		fib = prev1 + prev2
		prev1 = prev2
		prev2 = fib

	return fib



import math
def sherlockAndQueries(N, M, A, B, C):
	
	for i in range(0, M):
		for j in range(0, N):
			if j % B[i] == 0: A[j] = A[j] * C[i]

	A = [str(int(x % (math.pow(10,9) + 7))) for x in A]
	return A

'''
tmp = raw_input().split()
N = int(tmp[0])
M = int(tmp[1])

A = raw_input().split()
A = [int(x) for x in A]

B = raw_input().split()
B = [int(x) for x in B]

C = raw_input().split()
C = [int(x) for x in C]
'''

def isNestedProperly(s):
    stack = []
    
    characterPairMap = {')': '(', '}' : '{', ']' : '['}
    
    for c in s:
        if len(stack) > 0:
            top = len(stack)-1
            if characterPairMap.has_key(c) and stack[top] == characterPairMap[c]:
                del(stack[top])
            else:
                stack.append(c)
        else:    
            stack.append(c)
        
    return len(stack) == 0


print "here"
print isNestedProperly("(({})){}")

#ret = sherlockAndQueries(N, M, A, B, C)
#print ' '.join(ret)

'''
candies = [int(input()) for _ in range(0,n)]
candies.sort()
print angryChildren(n, k, candies)
'''


'''			
string = raw_input()
found = False
for word in itertools.permutations(string):
    if isPalindrome(word): 
    	found = True
    	break

if found:
	print 'YES'
else:
	print 'NO'
'''



