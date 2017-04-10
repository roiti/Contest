# -*- coding: utf-8 -*-
x, y, r = map(int, raw_input().split())
x1, y1, x2, y2 = map(int, raw_input().split())
x1 -= x
y1 -= y
x2 -= x
y2 -= y

red = blue = False
for x in xrange(-201, 201):
    for y in xrange(-201, 201):
        if x*x + y*y <= r*r and not (x1 <= x <= x2 and y1 <= y <= y2):
            red = True
        if not x*x + y*y <= r*r and x1 <= x <= x2 and y1 <= y <= y2:
            blue = True

print "YES" if red else "NO"
print "YES" if blue else "NO"
