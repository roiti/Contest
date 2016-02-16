# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
print sum(pow(i, n, 5) for i in xrange(1, 5)) % 5
