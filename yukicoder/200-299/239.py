N = int(raw_input())
A = [raw_input().split() for i in xrange(N)]
A = [[A[i][j] for i in xrange(N)] for j in xrange(N)]

ans = -1
for i in xrange(N):
	if A[i].count("nyanpass") == N - 1:
		if ans == -1:
			ans = i + 1
		else:
			print -1
			break
else:		
	print ans
