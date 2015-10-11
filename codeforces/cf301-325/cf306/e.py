# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = raw_input().split()
if a[-1] != "0":
    print "NO"
elif n == 1:
    print "YES"
    print a[0]
elif n >= 2:
    val = "1" == a[-2]
    if val:
        print "YES"
        print "->".join(a)
        exit()
    i = n - 3
    while i > -1 and not val:
        if a[i] == "0":
            val = True
            break
        i -= 1
    if val:
        ans = "->".join(a[:i]) + ("->(" if i > 0 else "(") + a[i] +"->(" + "->".join(a[i + 1:-1]) + "))->" + a[-1]
        print "YES"
        print ans
    else:
        print "NO"

