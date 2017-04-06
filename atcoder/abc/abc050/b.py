# -*- coding: utf-8 -*-
N = int(raw_input())
T = map(int, raw_input().split())
M = int(raw_input())
PX = [map(int, raw_input().split()) for i in xrange(M)]

S = sum(T)
for P, X in PX:
    print S - (T[P - 1] - X)

