#!
#! this is TLE solution
#!

import bisect
n, m = map(int, raw_input().split())
h = map(int, raw_input().split())
p = map(int, raw_input().split())

l, r = 0, 10 ** 15 + 1
ans = 10 ** 15 + 1
for loop in xrange(51):
	t = (l + r) / 2

	j = 0
	for i in xrange(n):
		if p[j] < h[i]:
			dl = h[i] - p[j]
			if dl > t: break
			while j <= m - 1:
				if p[j] <= h[i]:
					j += 1
				else:
					dr = p[j] - h[i]
					if p[j] <= h[i] + t - dl - min(dl, dr):
						j += 1
					else:
						break
		else:
			while j <= m - 1 and p[j] <= h[i] + t:
				j += 1

		if j == m:
			break

	if j == m:
		ans = min(ans, t)
		r = t
	else:
		l = t

print ans
