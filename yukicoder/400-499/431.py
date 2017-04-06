# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

D = map(int, raw_input().split())
print "SURVIVED" if sum(D[:3]) < 2 or D[3] else "DEAD"
