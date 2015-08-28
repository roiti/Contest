import itertools as it

bingos = ([[j for j in xrange(i, i + 5)] for i in xrange(1, 21, 5)] +
		[[j for j in xrange(i, 26, 5)] for i in xrange(1, 6)] +
		[[1, 7, 13, 19, 25], [5, 9, 13, 17, 21]])


prob = [0] * 26
for n in xrange(5, 26):
	fine = cnt = 0
	for hits in it.combinations(range(1, 26), n):
		for bingo in bingos:
			if all(i in hits for i in bingo):
				fine += 1
		cnt += 1
	prob[n] = 1.0 * fine / cnt

N = int(raw_input())
ans = 0
for i in xrange(5, N + 1):
	
	ans += prob[i]

print "%.10f" % ans
