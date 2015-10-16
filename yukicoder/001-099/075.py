# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def ok(k):
    dp = [0] * (K + 10)
    for i in xrange(1, K + 1):
        for j in xrange(1, 7):
            if j > i: dp[i] += k
            if i > j: dp[i] += dp[i - j]
        dp[i] = dp[i] / 6.0 + 1.0
    return dp[K] < m

K = int(raw_input())
l, r = 0.0, 1000.0
while r - l > 1e-5:
    m = (l + r) / 2
    if ok(m):
        r = m
    else:
        l = m
print "%.5f" % m;
