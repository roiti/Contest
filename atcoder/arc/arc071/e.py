# -*- coding: utf-8 -*- coding: utf-8 -*-
mod = 10**9 + 7
 
n, m = map(int, raw_input().split())
x = map(int, raw_input().split())
y = map(int, raw_input().split())
 
sx = sum(x)
sy = sum(y)
zx = 0
zy = 0
for i, xi in enumerate(x):
    zx += sx - (n - i)*xi
    sx -= xi
    zx %= mod
for i, yi in enumerate(y):
    zy += sy - (m - i)*yi
    sy -= yi
    zy %= mod
print zx*zy % mod
