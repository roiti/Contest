# -*- coding: utf-8 -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll
 
N, K = map(int, raw_input().split())
A = map(int, raw_input().split())
A = [i - 1 for i in A]
S = [raw_input() for i in xrange(N)]
 
if N == K:
    print 
    exit()
 
X = [S[i] for i in A]
Y = set([S[i] for i in xrange(N) if i not in set(A)])
mn = min(len(x) for x in X)
query = ""
 
flag = False
for i in xrange(mn):
    c = X[0][i]
    for j in xrange(1, K):
        if X[j][i] != c:
            flag = True
            break
    if flag:
        break
    else:
        query += c
        delist = []
        for y in Y:
            if y.startswith(query):
                break
            else:
                delist.append(y)
        else:
            print query
            exit()
        for y in delist:
            Y.remove(y)
     
for y in Y:
    if y.startswith(query):
        print -1
        break
else:
        print query
