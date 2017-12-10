# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
md = [map(int, raw_input().split("/")) for i in xrange(N)]

days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 1
yobi = 6
hurikae = 0
seq = 0
ans = 0
for month in xrange(1, 13):
    for day in xrange(1, days[month - 1] + 1):
        if [month, day] in md:
            if 5 <= yobi:
                hurikae += 1
            seq += 1
        elif 5 <= yobi:
            seq += 1
        else:
            if hurikae:
                seq += 1
                hurikae -= 1
            else:
                seq = 0
        ans = max(ans, seq)
        yobi = (yobi + 1) % 7
print ans
