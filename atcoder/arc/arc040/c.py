N = int(raw_input())
S = [list(raw_input()) for i in xrange(N)]
ans = 0
for r in xrange(N):
	for c in xrange(N - 1, -1, -1):
		if S[r][c] == ".":
			for i in xrange(c + 1):
				S[r][i] = "o"
			if r < N - 1:
				for i in xrange(c, N):
					S[r + 1][i] = "o"
			ans += 1
print ans
