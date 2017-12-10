T = int(raw_input())
for loop in xrange(T):
	N, K = map(int, raw_input().split())
	A = map(int, raw_input().split())

	piece, ans = K, 1
	for a in A:
		if a <= piece:
			piece -= a
		else:
			a -= piece
			ans += (a + K - 1) / K
			r = a % K
			piece = 0 if r == 0 else K - r
		piece = max(0, piece - 1)
	print ans
