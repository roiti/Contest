N = int(raw_input())
C = [int(raw_input()) for i in xrange(N)]

L = [0] * N
for i in xrange(N):
    for j in xrange(N):
        if i == j: continue
        if C[i] % C[j] == 0:
            L[i] += 1
ans = 0
for i in xrange(N):
    if L[i]% 2 == 0:
        ans += (L[i] + 2) * 1.0 / (2 * L[i] + 2)
    else:
        ans += 0.5
print "%.10f" % ans
