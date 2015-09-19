N = int(raw_input())
C = sorted([int(raw_input()) for i in xrange(N)])

L = [0] * N
for i in xrange(N):
    for j in xrange(i + 1, N):
        if C[j] % C[i] == 0:
            L[i] += 1
ans = N
for i in xrange(N):
    
    
