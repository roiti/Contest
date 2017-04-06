# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
s = raw_input()
t = raw_input()

for i in xrange(len(s)):
    for j in xrange(len(t)):
        if i + j >= len(s): continue
        if t[j] != s[i + j]:
            break
    else:
        print i + j + 1
        exit()
print len(s) + len(t)

