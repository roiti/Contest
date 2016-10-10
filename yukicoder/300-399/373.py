# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

A, B, C, D = map(int, raw_input().split())
print A*B%D*C%D
