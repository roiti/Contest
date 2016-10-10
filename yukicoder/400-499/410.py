# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

Px, Py = map(int, raw_input().split())
Qx, Qy = map(int, raw_input().split())
print (abs(Px - Qx) + abs(Py - Qy))/2.0
