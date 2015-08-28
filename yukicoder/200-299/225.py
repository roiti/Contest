def levenstein_distance(a, b):
	la, lb = len(a), len(b)
	if min(la, lb) == 0: return max(la, lb)

	A = [[0] * (lb + 1) for i in xrange(la + 1)]
	for i in xrange(la + 1): A[i][0] = i
	for i in xrange(lb + 1): A[0][i] = i

	for i in xrange(1, la + 1):
		for j in xrange(1, lb + 1):
			if a[i - 1] == b[j - 1]:
				A[i][j] = A[i - 1][j - 1]
			else:
				A[i][j] = min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1
	return A[la][lb]

n, m = map(int, raw_input().split())
s = raw_input()
t = raw_input()
print levenstein_distance(s, t)
