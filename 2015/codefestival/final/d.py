# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
S, T = [], []
for i in xrange(N):
    s, t = map(int, raw_input().split())
    S.append(s)
    T.append(t)
S.sort()
T.sort()

mx = 0 
top = -1
flag = False
si = ti = 0
on = []
for t in xrange(100005):
    while ti < N and T[ti] == t:
        ti += 1
        on.pop()
    while si < N and S[si] == t:
        change = True
        si += 1
        on.append(si)
    if len(on) > 0 and len(on) == mx:
        flag &= top == on[0]
    if len(on) > mx:
        mx = len(on)
        top = on[0]
        flag = True
ans = mx
if flag:
    ans -= 1
print ans

