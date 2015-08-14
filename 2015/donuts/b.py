import itertools
N,M = map(int,raw_input().split())
A = map(int,raw_input().split())
BCI = [map(int,raw_input().split()) for _ in xrange(M)]
B = [BCI[i][0]  for i in xrange(M)]
C = [BCI[i][1]  for i in xrange(M)]
I = [BCI[i][2:] for i in xrange(M)]
 
ans = 0
for unit in itertools.combinations(range(N),9):
    tmp = sum(A[i] for i in unit)
    for i in xrange(M):
        if tmp+sum(B[i:]) <= ans: break
        cnt = 0
        for j in xrange(C[i]):
            if I[i][j]-1 in unit:
                cnt += 1
        if cnt >= 3:
            tmp += B[i]
    ans = max(ans, tmp)
print ans
