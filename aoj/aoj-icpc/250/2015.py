from collections import defaultdict

def getArray(a):
    d = defaultdict(int)
    n = len(a)
    for i in range(n):
        s = 0
        for j in range(i,n):
            s += a[j]
            d[s] += 1
    return d

while 1:
    N,M = map(int,raw_input().split())
    if N == 0: break
    h = [int(raw_input()) for _ in xrange(N)]
    w = [int(raw_input()) for _ in xrange(M)]
    H,W = getArray(h),getArray(w)
    print sum(H[hi]*W[hi] for hi in H)

