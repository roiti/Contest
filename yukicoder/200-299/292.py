# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

S, i, j = raw_input().split()
S, i, j = list(S), int(i), int(j)

S[i] = S[j] = ""
print "".join(S)
