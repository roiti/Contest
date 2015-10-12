# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

x, y = map(int, raw_input().split())
ans = [] 
while x != y:
    if x < y:
        if y % x == 0:
            ans.append(str(y / x - 1) + "B")
            y = x
        else:
            ans.append(str(y / x) + "B")
            y %= x
    else:
        if x % y == 0:
            ans.append(str(x / y - 1) + "A")
            x = y
        else:
            ans.append(str(x / y) + "A")
            x %= y

if x != 1:
    print "Impossible"
else:
    print "".join(ans)

