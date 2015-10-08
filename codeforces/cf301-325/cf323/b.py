# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

MX = 110
n, T = map(int, raw_input().split())
a = map(int, raw_input().split())
a = a * min(T, MX)
m = len(a)
nums = [1] * m
for i in xrange(m - 1, -1, -1):
    tmp = 0
    for j in xrange(i + 1, min(m, i + 1 + 2 * n)):
        if a[j] >= a[i]:
            tmp = max(tmp, nums[j])
    nums[i] += tmp

if T <= MX:
    print max(nums)
else:
    ans = 0
    for i in xrange(n):
        ans = max(ans, nums[i] + (nums[i] - nums[i + n]) * (T - MX))
    print ans
