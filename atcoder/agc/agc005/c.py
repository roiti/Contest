# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def solve():
    N = int(raw_input())
    a = map(int, raw_input().split())
    if N == 2 and a == [1, 1]:
        return True

    cnt = [0]*(N + 1)
    for ai in a:
        cnt[ai] += 1

    mx = max(a)
    l, r = 0, mx
    for i in xrange(1, mx):
        l += 1
        r -= 1
        cnt[max(l, r)] -= 1

    if cnt[mx] < 2: return False
    for i in xrange(1, (mx + 1)/2 + 1):
        if cnt[i] > 0:
            return False
    for i in xrange(1, N):
        if cnt[i] < 0:
            return False
    return True

print "Possible" if solve() else "Impossible"
