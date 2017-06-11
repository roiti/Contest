# -*- coding: utf-8 -*-
N = int(raw_input())
a = map(int, raw_input().split()) 

over = 0
color = set()
for ai in a:
    if ai/400 >= 8:
        over += 1
    else:
        color.add(ai/400)

print max(1, len(color)), len(color) + over
