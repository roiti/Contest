# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = raw_input()
m = len(n)

if "8" in n:
    print "YES"
    print "8"
    exit()
if "0" in  n:
    print "YES"
    print "0"
    exit()

for i in xrange(m):
    for j in xrange(i + 1, m):
        if (int(n[i] + n[j])) % 8 == 0:
            print "YES"
            print n[i] + n[j]
            exit()

for i in xrange(m):
    for j in xrange(i + 1, m):
        for k in xrange(j + 1, m):
            if int(n[i] + n[j] + n[k]) % 8 == 0:
                print "YES"
                print n[i] + n[j] + n[k]
                exit()

print "NO"
