# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
s = raw_input()

two = {"0":0, "1":0}
three = False
cur = s[0]
cnt = 1
ans = 1
for si in s[1:]:
    if si == cur:
        cnt += 1
        if cnt == 2:
            two[si] += 1 
        if cnt == 3:
            three = True
    else:
        cur = si
        cnt = 1
        ans += 1
if (two["0"] + two["1"] >= 2) or three:
    ans += 2
elif max(two["0"], two["1"]) > 0:
    ans += 1
print ans
