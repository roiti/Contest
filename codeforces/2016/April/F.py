# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll
import urllib2

A = raw_input()
cnt = 5
url = "http://oeis.org/%s/list" % A

opner = urllib2.urlopen(url)
for line in opner.read().split("\n"):
    cnt += 1
    if cnt == 4:
        ans = ""
        i = line.index("<tt>") + 4
        while line[i] != "<":
            ans += line[i]
            i += 1

    if "a(n)" in line:
        cnt = 0

print ans
