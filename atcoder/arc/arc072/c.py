# -*- coding: utf-8 -*-
def solve(a):
    s, res = 0, 0
    for i, ai in enumerate(a):
        ss = s
        ss += ai
        if ss == 0:
            ss = 1 if s < 0 else -1
            res += 1
        else:
            if s < 0 and ss < 0:
                res += abs(ss) + 1
                ss = 1
            if s > 0 and ss > 0:
                res += abs(ss) + 1
                ss = -1
        s = ss
    return res

n = int(raw_input())
a = map(int, raw_input().split()) 

if a[0] == 0:
    a[0] = 1
    ans = solve(a) + 1
    a[0] = -1
    ans = min(ans, solve(a) + 1)
else:
    ans = solve(a)
    tmp = abs(a[0]) + 1
    a[0] = 1 if a[0] < 0 else -1
    ans = min(ans, solve(a) + tmp)
print ans

