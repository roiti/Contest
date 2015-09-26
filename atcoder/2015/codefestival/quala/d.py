# -*- coding: utf-8 -*-
N, M = map(int, raw_input().split())
X = [int(raw_input()) for i in xrange(M)]

def ok(t):
    x = 0
    for i in xrange(M):
        d = X[i] - x - 1
        if d <= 0:
            x = X[i] + t
            continue
        if d > t:
            break
        x = X[i] + max(0, t - 2 * d, (t - d) / 2)
        if x >= N: return True
    return x >= N 

if N == M:
    print 0
    exit()

l, r = 0, 2 * N
while r - l > 1:
    t = (l + r) / 2
    if ok(t): r = t
    else: l = t
print r
