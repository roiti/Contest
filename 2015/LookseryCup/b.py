import random
n = int(raw_input())
d = [map(int, list(raw_input())) for i in xrange(n)]
a = map(int, raw_input().split())
c = [0] * n

for loop in xrange(100000):
	v = [i for i in xrange(n) if a[i] == 0]
	if len(v) == 0:
		x = sum(c)
		print x
		print " ".join(map(str, [i + 1 for i in xrange(n) if c[i]]))
		exit()

	x = v[random.randint(0, len(v) - 1)]

	for y in xrange(n):
		if d[x][y]:
			if c[x]: a[y] += 1
			else: a[y] -= 1


	c[x] ^= 1


print -1
