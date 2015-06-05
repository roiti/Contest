import math,string,itertools as it,fractions,heapq,collections as collect,re,array,bisect,random

class TheLotteryBothDivs:
	def find(self, goodSuffixes):
		goodSuffixes = sorted(goodSuffixes , key = lambda x: len(x))
		suffixes = []
		for s in goodSuffixes:
			for i in xrange(len(s)):
				if s[i:] in suffixes:
					break
			else:
				suffixes.append(s)
				
		ans = 0
		for s in suffixes:
			ans += 0.1 ** len(s)
		return ans


#Powered by KawigiEdit-pf 2.3.0!
