import sys, math
from collections import deque

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

def lcm(lst):
    acc = 1
    allDone = False
    for i in lst:
        if allDone:
            break
        if i == 1:
            continue
        done = False
        while not done:
            tmp = filter(lambda x: x % i == 0, lst)
            if len(tmp) == 0:
                done = True
                continue
            acc *= i
            lst = [x / i if x % i == 0 else x for x in lst]
            tmp = filter(lambda x: x != 1, lst)
            if len(tmp) == 0:
                allDone = True

    return acc

def getPrimes():
    start = 2
    yield start

    while True:
        isPrime = True
        start += 1
        for i in xrange(2, int(math.sqrt(start)) + 1):
            if start % i == 0:
                isPrime = False

        if isPrime:
            yield start

def normalize_path(path, sep='/'):
    files = path.split(sep)
    acc = []

    for f in files:
        if f == '.': 
            continue
        elif f == '..':
            prev_index = len(acc) - 1
            if prev_index >= 0:
                del(acc[prev_index])
                continue

        acc.append(f)

    return sep.join(acc)

def increment_array(array):
    acc = 1
    count = len(array)
    i = count - 1
    while i >= 0:
        mult = (10 ** (count - i - 1)) * int(array[i])
        acc += mult
        i -= 1

    return list(str(acc))

def to_decimal(val, base=2):
    acc = 0
    chars = list(val)
    count = len(chars)
    i = count - 1
    while i >= 0:
        mult = (base ** (count - i - 1)) * int(chars[i])
        acc += mult
        i -= 1

    return acc

def is_power_of_two(d):
    while d > 2:
        d = d / 2
        if d % 2 != 0:
            return False
    return True

def is_anagram(s1, s2):
    h1 = {}
    h2 = {}
    for c in s1:
        if not h1.has_key(c):
            h1[c] = 0
        h1[c] += 1

    for c in s2:
        if not h2.has_key(c):
            h2[c] = 0
        h2[c] += 1

    if len(h1) != len(h2):
        return False

    for k,v in h1.iteritems():
        if v != h2.get(k):
            return False

    return True


class SNode(object):

    def __init__(self, value, nodeList):
        self.value = value
        self.nodeList = nodeList

def traverseSuffixTree2(node, acc=None):
    if acc is None:
        acc = []

    acc.append(node.value)
    if node.nodeList is None:
        tmp = "".join(acc)
        return [tmp]

    res = []
    for n in node.nodeList:
        res += traverseSuffixTree2(n, acc)
        acc = [node.value]

    return res

def traverseSuffixTree3(node):
    queue = [node]

    acc = []
    res = []
    rootChar = node.value
    while len(queue):
        curNode = queue[len(queue)-1]
        del(queue[len(queue)-1])
        acc.append(curNode.value)
        if curNode.nodeList:
            for n in curNode.nodeList:
                queue.append(n)
        else:
            res.append("".join(acc))
            acc = [rootChar]

    return res



def traverseSuffixTree(c, root, acc=None):
    if acc is None:
        acc = []

    if root is None:
        tmp = "".join(acc)
        return [tmp]

    res = []
    for k, v in root.iteritems():
        if k != c:
            acc.append(k)
        res += traverseSuffixTree(k, v, acc)
        acc = []

    
    return res

def genSurpasserList(lst):
    count = len(lst)
    ret = [0] * count
    for i in xrange(0, count-1):
        numGt = 0
        for j in xrange(i+1, count):
            if lst[j] > lst[i]:
                numGt += 1
        ret[i] = numGt

    return ret

def getShortestSubsequence(s, lst):
    if not s or not len(lst):
        return ""

    startIndexes = []
    endIndexes = []
    startWord = lst[0]
    endWord = lst[len(lst) - 1]
    words = s.split(" ")

    # store indexes of start and end of sequence
    for i in xrange(0, len(words)):
        if words[i] == startWord:
            startIndexes.append(i)
        elif words[i] == endWord:
            endIndexes.append(i)

    shortestSubsequence = []
    subsequenceExists =  False
    for i in startIndexes:
        for j in endIndexes:
            if j > i:
                curIndex = 1

                # look in possible range for candidates
                for k in xrange(i + 1, j):
                    if curIndex >= len(lst):
                        break
                    if words[k] == lst[curIndex]:
                        curIndex += 1

                if curIndex >= len(lst) - 1:
                    candidate = words[i:j+1]
                    if subsequenceExists:
                        shortestSubsequence = candidate if len(candidate) < len(shortestSubsequence) \
                                                else shortestSubsequence
                        subsequenceExists = True
                    else:
                        shortestSubsequence = candidate

    return " ".join(shortestSubsequence)



def sumUpToExists(n, lst):
    hash = {}
    for i in lst:
        if not hash.has_key(i):
            hash[i] = 1
        else:
            hash[i] += 1

    for i in lst:
        k = n - i

        if not hash.has_key(k):
            continue

        if k == (n / 2):
            if hash[k] > 1:
                return True
        elif hash[k]:
            return True

    return False

def maxSubArraySum(arr):
    allNegative = filter(lambda x: x >= 0, arr)
    if len(arr) == 0:
        return max(arr)

    globMax = 0
    localMax = 0
    for i in xrange(0, len(arr)):
        tmp = localMax + arr[i]
        if tmp > 0:
            localMax += arr[i]
        else:
            localMax = 0
        if localMax > globMax:
            globMax = localMax

    return globMax    

    
if __name__ == "__main__":

    print maxSubArraySum([1, -3, 2, -5, 7, 6, -1, -4, 11, -23])

    # print sumUpToExists(8, [5, 1, 2, 4])

    # sentence = """
    # One Ring to rule them all, One Ring to find them, One Ring to bring them all find them, all and in the darkness bind them"
    # """
    # words = ["find", "them,", "all"]
    # candidate = getShortestSubsequence(sentence, words)
    # print candidate

    # print genSurpasserList([2, 7, 5, 5, 2, 7, 0, 8, 1])

    # s = SNode('s', None)
    # o = SNode('o', [s])
    # m = SNode('m', [o])
    # e2 = SNode('e', None)
    # c = SNode('c', [e2])
    # e = SNode('e', None)
    # b = SNode('b', [e])
    # a = SNode('a', [b, c, m])

    # print traverseSuffixTree3(a)

    # suffixTree = {
    #               'a' : {
    #                   'b' : {
    #                       'e' : None
    #                   },
    #                   'c' : {
    #                       'e' : None
    #                   },
    #                   'm' : {
    #                       'o' : {
    #                           's' : None
    #                       }
    #                   }
    #               }

    #           }

    # print traverseSuffixTree('a', suffixTree)

    # count = 0
    # for p in getPrimes():
    #   print p
    #   count += 1
    #   if count == 10001:
    #       break

    # print lcm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    # sortedLists = [
    #   [1, 2, 3, 4, 5],
    #   [6, 7, 8, 8, 9, 10],
    #   [11, 12, 13, 14, 15, 16, 16],
    #   [1, 2, 3, 4, 5],
    # ]

    # print nWayMerge(sortedLists)


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
    #   print i
    #   count += 1
    #   if count > 5: 
    #       break
    # 