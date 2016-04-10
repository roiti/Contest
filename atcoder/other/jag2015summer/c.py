# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def rec(s):
    if s == "ABC": return True
    if len(s) <= 3: return False
    res = False
    for c in "ABC":
        if c + c not in s:
            t = s.replace("ABC", c)
            res |= rec(t)
    return res

S = raw_input()
print "Yes" if rec(S) else "No"
A = "ABC"
j = 0
for i in xrange(2400):
    B = ""
    for c in A:
        if c == "C":
            B += "ABC"
        else:
            B += c
    A = B
    j = (j + 1)%3
print A

