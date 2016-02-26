# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
B = int(raw_input())
a = map(float, raw_input().split())

f_div_B = sum(ai*B**(ai - 1) for ai in a)
F_B = sum(1.0/(ai + 1)*B**(ai + 1) if ai != -1.0 else math.log(B) for ai in a)
print "%.10f" % f_div_B
print "%.10f" % F_B
