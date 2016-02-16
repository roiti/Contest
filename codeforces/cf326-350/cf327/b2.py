# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

alpha = list("abcdefghijklmnopqrstuvwxyz")

n, m = map(int, raw_input().split())
s = raw_input()
for i in xrange(m):
    x, y = raw_input().split()
    x = ord(x) - ord("a")
    y = ord(y) - ord("a")
    alpha[x], alpha[y] = alpha[y], alpha[x]

dic = {alpha[i]:chr(ord("a") + i) for i in xrange(26)}
ans = "".join(dic[s[i]] for i in xrange(n))
print ans
