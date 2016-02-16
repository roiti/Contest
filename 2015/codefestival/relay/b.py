# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

p = [raw_input() for i in xrange(10)]
print "Yes" if all(any(p[y][x] == "o" for y in xrange(10)) for x in xrange(10)) else "No"
