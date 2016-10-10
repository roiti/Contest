# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

M = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
W = [ "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

s = raw_input()
t = raw_input()

x = W.index(s)
y = W.index(t)

for i in xrange(11):
    if M[i]%7 == (y - x)%7:
        print "YES"
        break
else:
    print "NO"
