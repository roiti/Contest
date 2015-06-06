N, M = map(int, raw_input().split())
A = [list(raw_input()) for i in xrange(N)]
A = [[{"W":1, "B":-1}[A[i][j]] for j in xrange(M)] for i in xrange(N)]
B = [[A[N - 1][M - 1]] * M for i in xrange(N)]

ans = 1
for x in xrange(M - 1, -1, -1):
	for y in xrange(N - 1, -1, -1):
		if A[y][x] == B[y][x]: continue
		d = A[y][x] - B[y][x]
		for yi in xrange(y, -1, -1):
			for xi in xrange(x, -1, -1):
				if (xi, yi) == (x, y): continue
				B[yi][xi] = (B[yi][xi] + d)
		ans += 1
print ans
