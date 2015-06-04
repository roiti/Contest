#SRM660 Div1 Easy
import math,string,itertools as it,fractions,heapq,collections as collect,re,array,bisect,random,sys

class Coversta:
	def place(self, a, x, y):
		n, m, k = len(a), len(a[0]), len(x)
		a = [map(int, list(a[i])) for i in xrange(n)]
		dwr = zip(x, y)

		scores = []
		for w in xrange(n):
			for r in xrange(m):
				tmp = 0
				for dw, dr in dwr:
					nw, nr = w + dw, r + dr
					if 0 <= nw < n and 0 <= nr < m:
						tmp += a[nw][nr]
				scores.append([tmp, w, r])

		scores = sorted(scores, key = lambda z:z[0], reverse = True)
		ans = 0
		for i in xrange(min(k * k + 1, n * m)):
			s, w, r = scores[i]
			cover1 = set((w + dw, r + dr) for dw, dr in dwr)
			for j in xrange(i + 1, min(k * k + 1, n * m)):
				ss, ww, rr = scores[j]
				cover2 = set((ww + dw, rr + dr) for dw, dr in dwr)
				tmp = s + ss
				for p, q in cover1 & cover2:
					if 0 <= p < n and 0 <= q < m:
						tmp -= a[p][q]
				ans = max(ans, tmp)

		return ans
