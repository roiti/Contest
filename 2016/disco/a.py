# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

s = "DiscoPresentsDiscoveryChannelProgrammingContest2016"
W = int(raw_input())
for i in xrange(0, len(s), W):
    print s[i:i+W]

