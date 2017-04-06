# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, K = map(int, raw_input().split())
print K*(K-1)**(N-1)
