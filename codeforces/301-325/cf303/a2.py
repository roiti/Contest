n = int(raw_input())
A = [map(int, raw_input().split()) for i in xrange(n)]
ans = [1] * n
for i in xrange(n):
    for j in xrange(n):
        if A[i][j] == 1 or A[i][j] == 3:
            ans[i] = 0
print sum(ans)
