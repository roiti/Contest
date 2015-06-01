N,M = map(int,raw_input().split())
B = map(int,raw_input().split())
P = map(int,raw_input().split())
C1,C2 = [],[]
for i in xrange(M):
    C1 += [1]*P[i] if i%2 else [0]*P[i]
    C2 += [0]*P[i] if i%2 else [1]*P[i]

ans = 1e10
for C in [C1,C2]:
    if sum(B) == sum(C):
        tmp = 0
        i = j = 0
        while not i == j == N-1:
            if not B[i]: i = min(N-1, i+1)
            if not C[j]: j = min(N-1, j+1)
            if B[i] and C[j]:
                tmp += abs(i-j)
                i = min(N-1, i+1)
                j = min(N-1, j+1)
        ans = min(ans, tmp)
print ans



