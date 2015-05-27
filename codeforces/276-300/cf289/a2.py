n = int(raw_input())
A = [[1]*n for i in xrange(n)]
for i in xrange(1,n):
    for j in xrange(1,n):
        A[i][j] = A[i-1][j]+A[i][j-1]
print A[-1][-1]
