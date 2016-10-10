# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, A, B = map(int, raw_input().split())
S = raw_input()
p, q = 0, 0
for s in S:
    if s == "a":
        if p + q < A + B:
            print "Yes"
            p += 1
        else:
            print "No"
    if s == "b":
        if p + q < A + B and q < B:
            print "Yes"
            q += 1
        else:
            print "No"
    if s == "c":
        print "No"
