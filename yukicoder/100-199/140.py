mod = 10**9+7

N = int(raw_input())
C = [[0]*(N+2) for i in xrange(N+2)]
F = [[0]*(N+2) for i in xrange(N+2)]
P = [[0]*(N+2) for i in xrange(N+2)]

for i in xrange(N+1):
    C[i][0] = 1
    for j in xrange(1,i+1):
        C[i][j] = (C[i-1][j-1] + C[i-1][j]) % mod

for i in xrange(1,N+1):
    F[i][1] = 1
    for j in xrange(2,i+1):
        F[i][j] = (F[i-1][j-1] + j * F[i-1][j]) % mod

for i in xrange(N+1):
    P[i][0] = 1
    for j in xrange(N+1):
        P[i][j+1] = P[i][j] * i * (i-1) % mod

ans = 0
for i in xrange(1,N+1):
    for j in xrange(1,i+1):
        ans = (ans + C[N][i] * F[i][j] * P[j][N-i]) % mod

print ans