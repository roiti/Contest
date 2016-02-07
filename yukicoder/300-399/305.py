# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

ans = ""
for i in xrange(10):
    mx, k = 0, -1
    for j in xrange(10):
        tmp = "0" * (10 - i - 1) + str(j) + ans
        print tmp
        sys.stdout.flush()
        hit, res = raw_input().split()
        if res == "unlocked":
            exit()
        hit = int(hit)
        if hit > mx:
            mx = hit
            k = j 
    ans = str(k) + ans
print ans
res = raw_input()
