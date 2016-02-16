# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

c = list(raw_input())

s = "ox"
h = 0
while len(set(c)) == 2:
    if c[0] == s[1 - h]:
        for i in xrange(len(c)):
            if c[i] == s[h]: break
            c[i] = s[h] 
        c = [s[h]] + c
    elif c[-1] == s[1 - h]:
        for i in xrange(len(c) - 1, -1, -1):
            if c[i] == s[h]: break
            c[i] = s[h] 
        c = c + [s[h]]
    h = 1 - h
print c[0]
