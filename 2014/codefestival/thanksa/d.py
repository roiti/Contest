# coding: utf-8
n,q = map(int,raw_input().split())
for roop in range(q):
    a,b,s,t = map(int,raw_input().split())
    if   a <= s <= t <= b: print 0
    elif a <= s <= b <= t: print 100*(t-b)
    elif s <= a <= t <= b: print 100*(a-s)
    elif s <= a <= b <= t: print 100*(t-s-(b-a))
    else: print 100*(t-s)
