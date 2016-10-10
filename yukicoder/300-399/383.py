# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

a, b = map(int, raw_input().split())
if a == b: print 0
if a  > b: print "-%d" % (a - b)
if a  < b: print "+%d" % (b - a)
