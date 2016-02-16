# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

mod = 10**9 + 7

x, y = map(int, raw_input().split())
n = int(raw_input())
ans = [x, y, y - x, -x, -y, x - y, x]
print (ans[(n - 1) % 6] + mod) % mod
