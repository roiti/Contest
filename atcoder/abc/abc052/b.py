# -*- coding: utf-8 -*-
N = int(raw_input())
S = raw_input()
ans = cur = 0
for s in S:
    if s == "I":
        cur += 1
    else:
        cur -= 1
    ans = max(ans, cur)
print ans
