R = 1 << 12
b = [0] * R

n = int(raw_input())
for i in xrange(n):
	s = raw_input()
	for j in xrange(12):
		if s[j] == "o":
			b[i] |= 1 << j

e = [0] * R
for i in xrange(n):
	e[b[i]] = 1

dp = [0] * R
b = [1] * R
mask = R - 1
for i in xrange(R):
	x = 0
	for j in xrange(1, R):
		if not e[j] or (i & j) == 0: continue
		t = dp[i & (j ^ mask)] + 1
		if x < t:
			x = t
	dp[i] = x

print dp[mask]
