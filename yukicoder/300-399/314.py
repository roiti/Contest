#-*- coding: utf-8 -*-
mod = 10**9 + 7
N = int(raw_input())
# 「ケン」からスタート
ken0, ken1, ken2 = 0, 1, 0
for i in xrange(1, N):
    #「パ」になる場合
    nken0 = (ken1 + ken2) % mod
    #1回めの「ケン」で進む場合
    nken1 = ken0
    #2回めの「ケン」で進む場合
    nken2 = ken1
    ken0, ken1, ken2 = nken0, nken1, nken2
print (ken0 + ken1 + ken2) % mod

