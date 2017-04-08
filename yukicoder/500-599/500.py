# -*- coding: utf-8 -*-
N = int(raw_input())
ans = 1
for i in xrange(1, min(1000, N + 1)):
    ans = ans * i
print str(ans)[-12:]
