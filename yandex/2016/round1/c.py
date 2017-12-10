# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

point = [100, 75, 60, 50, 45, 40, 36, 32, 29, 26, 24, 22, 20, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

score = map(int, raw_input().split())
score.sort()
score = [score[0]]*20 + score

ans = 0
# rank < 30
worst = 1
i = 0
for j in xrange(30):
    if score[j] >= 0:
        worst += 1
    elif score[j] + point[i] >= 0:
        worst += 1
        i += 1
if worst <= 10:
    ans = 1000

# rank >= 30
for rank in xrange(30):
    worst = 1
    p = [point[i] for i in xrange(30) if i != rank]
    i = 0
    for j in xrange(30):
        if score[j] - point[rank] >= 0:
            worst += 1
        elif i < 29 and score[j] - point[rank] + p[i] >= 0:
            worst += 1
            i += 1
    if worst <= 10:
        ans = max(ans, rank + 1)

print ans 

