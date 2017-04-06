# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

A, B, C = map(int, raw_input().split())
print min(B*C*(A - A/2*2), C*A*(B - B/2*2), A*B*(C - C/2*2))
