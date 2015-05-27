# coding: utf-8
ref = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = int(raw_input())
ans = 10**32
for loop in xrange(N):
    v = raw_input()
    base = 1
    for vi in v:
        base = max(base, ref.index(vi)+1)
    ans = min(ans, sum(ref.index(v[-i-1])*base**i for i in xrange(len(v))))
print ans    
