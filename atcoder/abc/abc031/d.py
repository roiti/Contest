# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def dfs(i, j):
    if i == len(V) and j == len(W):
        ans = sorted([[v, w] for v, w in dic.items()], key = lambda x:int(x[0]))
        for v, w in ans:
            print w
        return True
    if i >= len(V) or j >= len(W):
        return False
    if V[i] == W[j] == ",":
        return dfs(i + 1, j + 1)
    if (V[i] == "," and W[j] != ",") or (V[i] != "," and W[j] == ","):
        return False
    if V[i] not in dic:
        for k in xrange(1, 4):
            if j + k > len(W): break
            if W[j + k - 1] == ",": break
            dic[V[i]] = W[j:j + k]
            res = dfs(i + 1, j + k)
            if res: return True
            del dic[V[i]]
        return False
    else:
        w = dic[V[i]]
        for k in xrange(len(w)):
            if j + k >= len(W) or w[k] != W[j + k]:
                return False
        return dfs(i + 1, j + len(w))

K, N = map(int, raw_input().split())
V, W = "", ""
for i in xrange(N):
    v, w = raw_input().split()
    V += "," + v
    W += "," + w
V = V[1:]
W = W[1:]
dic = {}
dfs(0, 0)
