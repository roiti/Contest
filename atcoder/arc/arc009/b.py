b = raw_input().split()
t = dict(zip(b, map(str, range(10))))
r = dict(zip(map(str, range(10)), b))
N = int(raw_input())
num = sorted([int("".join([t[c] for c in raw_input()])) for i in xrange(N)])
for n in num:
    print "".join(r[c] for c in str(n))
