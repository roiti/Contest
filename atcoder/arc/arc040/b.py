N, R = map(int, raw_input().split())
S = list(raw_input())
ans = 0
r = 0
for i in xrange(N - 1, -1, -1):
	if S[i] == ".":
		for j in xrange(i, max(-1, i - R), -1):
			if S[j] == ".":
				S[j] = "o"
		r = max(r, i - R + 1)
		ans += 1
print ans + r
