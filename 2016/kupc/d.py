# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll
import random

N = int(raw_input())
t = [[".","."], [".", "#"], ["#", "."], ["#", "#"]]
s1, s2 = "", ""

left = True
for loop in xrange(421):
    random.shuffle(t)
    if left:
        for t1, t2 in t: 
            print "\n".join([s1 + t1, s2 + t2])
            sys.stdout.flush()
            res = raw_input()
            if res == "T":
                s1 += t1
                s2 += t2
                break
            if res == "end":
                exit()
        else:
            left = False

    if not left:
        for t1, t2 in t:
            print "\n".join([t1 + s1, t2 + s2])
            sys.stdout.flush()
            res = raw_input()
            if res == "T":
                s1 = t1 + s1
                s2 = t2 + s2
                break
            if res == "end":
                exit()
