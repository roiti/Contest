# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
A = map(int, raw_input().split())
v = int(raw_input())
print sum(A) - v
