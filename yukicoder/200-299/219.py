#coding: utf-8

"""落ちるケースがある可能性が・・・"""
from math import log10
N = int(raw_input())
for loop in xrange(N):
    A, B = map(int, raw_input().split())
    t = int(B * log10(A))
    a = "%.16f" % 10 ** (B * log10(A) - t)
    x, y = a[0], a[2]
    print x, y, t
