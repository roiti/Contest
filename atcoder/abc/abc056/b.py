# -*- coding: utf-8 -*-
W, a, b = map(int, raw_input().split())
print 0 if a <= b <= a + W or a <= b + W <= a + W else min(abs(b - (a + W)), abs(a - (b + W)))
