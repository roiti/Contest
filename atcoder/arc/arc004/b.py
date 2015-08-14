N = int(raw_input())
d = [int(raw_input()) for i in xrange(N)]
a = max(d)
mx = sum(d)
mn = 0 if a - (mx - a) <= 0 else a - (mx - a)
print mx
print mn
