# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

S = raw_input()
ab, ba = [], []
for i in xrange(len(S) - 1):
    if S[i:i + 2] == "AB":
        ab.append(i)
    if S[i:i + 2] == "BA":
        ba.append(i)
if ab and ba and (ab[0] + 1 < ba[-1] or ba[0] + 1 < ab[-1]):
    print "YES"
else:
    print "NO"
