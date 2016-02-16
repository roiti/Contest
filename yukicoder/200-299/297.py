# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = raw_input().split()

x = ""
p = m = 0
for c in a:
    if c == "+": p += 1
    elif c == "-": m += 1
    else: x += c

x = sorted(x, reverse = True)
y = x[:]
nums = []
for i in xrange(p + m):
    nums.append(int(x.pop()))
nums.append(int("".join(x)))
nums = nums[::-1]

mx = nums[0]
mn = nums[-1]
for i in xrange(p + m):
    if i < p:
        mx += nums[i + 1]
        mn += nums[-i - 2]
    else:
        mx -= nums[i + 1]
        mn -= nums[-i - 2]
if m == 0:
    nums = [""] * (p + 1)
    i = 0
    while y:
        nums[i%(p+1)] = y.pop(0) + nums[i%(p+1)]
        i += 1
    mn = sum(map(int, nums))
print mx, mn
