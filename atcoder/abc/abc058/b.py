# -*- coding: utf-8 -*-
O = raw_input()
E = raw_input()

ans = [""]*(len(O) + len(E))
for i, o in enumerate(O):
    ans[2*i] = o
for i, e in enumerate(E):
    ans[2*i + 1] = e
print "".join(ans)
