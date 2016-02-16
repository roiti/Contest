# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

S = raw_input()
for loop in xrange(100):
    for i in xrange(200):
        S = S.replace("--", "")
    for i in xrange(200):
        S = S.replace("!-", "!")
    p = 0
    for i in xrange(len(S) - 1, -1, -1):
        if S[i] == "!":
            p = i
            break
    T = S[:p]
    for i in xrange(200):
        T = T.replace("!!","")
    S = T + S[p:]
print S
