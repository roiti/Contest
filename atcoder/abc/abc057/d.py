# -*- coding: utf-8 -*-
from collections import Counter

def combinations(n, r):
    res = 1
    for i in xrange(n - r + 1, n + 1):
        res *= i
    for i in xrange(2, r + 1):
        res /= i
    return res

N, A, B = map(int, raw_input().split())
v = map(int, raw_input().split())
v.sort(reverse = True)
cnt = Counter(v)

mx = sum(v[:A]) 
comb = 0
for n in xrange(A, B + 1):
    tmp = 1
    for key, val in Counter(v[:n]).items():
        tmp *= combinations(cnt[key], val)

    if A*sum(v[:n]) == n*mx:
        comb += tmp 

print "%.10f" % (mx*1.0/A)
print comb 
