N, X, Y, Z = map(int, raw_input().split())
X, Y, Z = X - 1, Y - 1, Z - 1
diag = set([(0, 0), (0, 3), (1, 1), (1, 2), (2, 1), (2, 2), (3, 0), (3, 3)])

A = [[-1] * N for i in xrange(N)]
for r in xrange(N):
	for w in xrange(N):
		if (w % 4, r % 4) in diag:
			A[r][w] = w + N * r

for r in xrange(N):
	for w in xrange(N):
		if A[N - r - 1][N - w - 1] == -1:
			A[N - r - 1][N - w - 1] = w + N * r

bit = A[Y][X]
for r in xrange(N):
	for w in xrange(N):
		A[r][w] ^= Z ^ bit
		A[r][w] += 1

for line in A:
	print " ".join(map(str, line))
