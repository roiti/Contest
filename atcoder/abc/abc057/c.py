# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def fact(n):
    i = 2
    res = []
    while i*i <= n:
        while n % i == 0:
            res.append(i)
            n /= i
        i += 1
    res.append(n)
    return sorted(res)

def dfs(array, a, b, pos):
    if len(array) == pos:
        return max(len(str(a)), len(str(b)))
    return min(dfs(array, a*array[pos], b, pos + 1), dfs(array, a, b*array[pos], pos + 1))

N = int(raw_input())
f = fact(N)
print dfs(f, 1, 1, 0)
