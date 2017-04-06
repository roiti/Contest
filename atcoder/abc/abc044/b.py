# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

w = raw_input()
cnt = [0]*26
for c in w:
    cnt[ord(c) - ord("a")] += 1
print "Yes" if all([cnt[i]%2 == 0 for i in xrange(26)]) else "No"
