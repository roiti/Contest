#SRM506 Div1Easy
import math,string,itertools as it,fractions,heapq,collections as collect,re,array,bisect,random,sys

class SlimeXSlimesCity:
	def merge(self, _P):
		ans = 0
		n = len(_P)
		for i in xrange(n):
			P = list(_P)
			c = P.pop(i)
			while P:
				update = False
				for j in xrange(len(P)):
					if c >= P[j]:
						c += P.pop(j)
						update = True
						break
				if not update:
					break
			else:
				ans += 1

		return ans
