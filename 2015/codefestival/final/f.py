# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

_C = map(int, raw_input().split())
ans = False

C = _C[:]
#一周
C[0] -= 1
ans |= sum(C) == 0
for i in xrange(7):
    C[i] -= 1
for i in xrange(7):
    d = min(C[(i + 1)%7], C[i])
    d = max(d, 0)
    C[i] -= d
    C[(i + 1)%7] -= d
ans |= sum(map(abs,C)) == 0

#行って帰ってくる
C = _C[:]
for i in xrange(6, 0, -1):
    if C[i] == 0: continue
    for j in xrange(i, 0, -1):
        C[j - 1] -= C[j]
        if C[j - 1] <= 0:
            break
        C[j] = 0
    else:
        ans |= C[0] == 1
    break

#行って帰って行って帰って
for i in xrange(6, 0, -1):
    C = _C[:]
    if C[i] > 0:
        ok = True
        for j in xrange(i, 0, -1):
            C[j - 1] -= C[j]
            if C[j - 1] <= 0:
                ok = False
                break
            C[j] = 0
        if not ok: continue
        for j in xrange(i + 1, 7):
            C[(j + 1)%7] -= C[j%7]
            if C[j%7] > 0 and C[(j + 1)%7] <= 0:
                ok = False
                break
            C[j%7] = 0
        if ok:
            ans |= C[0] == 1
print "YES" if ans else "NO"
