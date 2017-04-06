# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, K = map(int, raw_input().split())
A = map(int, raw_input().split())
A = [i - 1 for i in A]
S = [raw_input() for i in xrange(N)]

if N == K:
    print 
    exit()

X = [S[i] for i in A]
mn = min(len(x) for x in X)
query = ""

flag = False
for i in xrange(mn):
    c = X[0][i]
    for j in xrange(1, K):
        if X[j][i] != c:
            flag = True
            break
    else:
        query += c
    if flag:
        break

B = [i for i in xrange(N) if i not in set(A)]
mx = 0
l = len(query)
for i in B:
    for j in xrange(len(S[i])):
        if S[i][j] != query[j]:
            mx = max(mx, j)
            break
        elif j + 1 >= l:
            print -1
            exit()
    else:
        mx = max(mx, len(S[i]))

print query[:mx + 1]
