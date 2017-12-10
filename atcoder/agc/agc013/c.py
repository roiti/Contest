# -*- coding: utf-8 -*-

inf = 10**10

N, L, T = map(int, raw_input().split())
XW = [map(int, raw_input().split()) for i in xrange(N)]
T %= L
A = [0]*N

for i, (x, w) in enumerate(XW):
    A[i] = (x + (3 - 2*w)*T + inf*L)%L

x, w = XW[0]
cnt = 0
if w == 1:
    for xx, ww in XW[1:]: 
        if ww == 1: continue
        if 2*T - (xx - x) < 0: continue
        cnt += 1 + (2*T - (xx - x))/L
else:
    for xx, ww in XW[1:]: 
        if ww == 2: continue
        if 2*T - (L - (xx - x)) < 0: continue
        cnt -= 1 + (2*T - (L - (xx - x)))/L
cnt = (cnt + inf*N)%N
for i in xrange(N):
    print A[(i - cnt + N)%N]
