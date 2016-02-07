# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

xa, ya = map(float, raw_input().split())
xb, yb = map(float, raw_input().split())
xb *= -1

y = (ya - yb)/(xa - xb) * (0 - xa) + ya
print "%.10f" % y
