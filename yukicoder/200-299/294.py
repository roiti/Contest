# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def comb(n, r):
    res = 1
    for i in xrange(r):
        res *= n - i
    for i in xrange(1, r + 1):
        res /= i
    return res

def bitcount(x):
    x = (x & 0x5555555555555555) + (x >> 1 & 0x5555555555555555)
    x = (x & 0x3333333333333333) + (x >> 2 & 0x3333333333333333)
    x = (x & 0x0f0f0f0f0f0f0f0f) + (x >> 4 & 0x0f0f0f0f0f0f0f0f)
    x = (x & 0x00ff00ff00ff00ff) + (x >> 8 & 0x00ff00ff00ff00ff)
    x = (x & 0x0000ffff0000ffff) + (x >> 16 & 0x0000ffff0000ffff)
    return (x & 0x00000000ffffffff) + (x >> 32 & 0x00000000ffffffff)

ans = 0
N = int(raw_input())
#3は5n個、5は3m個。1桁目は必ず5
for k in xrange(3, 26):
    cnt = 0
    for i in xrange(3, k + 1, 3):
        j = k - i
        cnt += comb(j + i - 1, i - 1)
    if N > cnt:
        N -= cnt
    else:
        x = -1
        while N:
            x += 2
            if bitcount(x) % 3 == 0: N -= 1
        ans = bin(x)[2:].zfill(k).replace("0", "3").replace("1", "5")
        break
    if ans > 0: break
print ans
