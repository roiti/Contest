# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
S = raw_input()

if N >= 4:
    print "YES"
else:
    if "11" in S or "00" in S:
        print "YES"
    else:
        print "NO"

