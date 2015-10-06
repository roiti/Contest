# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll
mod = 10 ** 9 + 7

n = int(raw_input())
print (pow(27, n, mod) - pow(7, n, mod)) % mod
