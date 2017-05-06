# -*- coding: utf-8 -*-

A, B, C = map(int, raw_input().split())

ans = 0
while not (A%2 or B%2 or C%2 or A == B == C):
    A, B, C = (B + C)/2, (C + A)/2, (A + B)/2
    ans += 1
print ans if not A == B == C else -1 if A%2 == 0 else 0

