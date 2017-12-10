# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll
def lcs(seq1, seq2):
    a, b = len(seq1), len(seq2)
    x1 = [0 for i in range(b+1)]
    for i in range(a):
        e1 = seq1[i]
        x2 = x1+[]
        for j in range(b):
            if e1 == seq2[j]:
                x1[j+1] = x2[j] + 1
            elif x1[j+1] < x1[j]:
                x1[j+1] = x1[j]
    return x1[-1]

S = raw_input()
T = raw_input()
NS, NT = len(S), len(T)
subS, subT = set(), set()
mx = lcs(S, T)
for n in xrange(1, NS + 1):
    for select in it.combinations(range(NS), n):
        U = "".join([S[i] for i in select])
        subS.add(U)
for n in xrange(1, NT + 1):
    for select in it.combinations(range(NT) , n):
        U = "".join([T[i] for i in select])
        subT.add(U)

sub = subS & subT
ans = []
for U in sub:
    if lcs(T, U) == lcs(S, U) == mx:
        ans.append(U)

ans.sort()
if len(ans) == 0:
    print 1
    print ""
else:
    print len(ans)
    for U in ans:
        print U
