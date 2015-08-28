N, M = map(int, raw_input().split())
fill = [0] * M
for loop in xrange(N):
    L, R = map(int, raw_input().split())
    for i in xrange(L, R + 1):
        fill[i] += 1
        fill[M - i - 1] += 1
print "YES" if max(fill) <= 2 else "NO"

