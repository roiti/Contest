# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

Ma, Da = map(int, raw_input().split())
Mb, Db = map(int, raw_input().split())

ans = sum(days[:Mb - 1]) + Db - sum(days[:Ma - 1]) - Da
print ans

