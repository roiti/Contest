from collections import defaultdict
used = defaultdict(int)
A,B,X = map(int,raw_input().split())
for t in xrange(1000000001):
    if A == X:
        print t
        break
    A = (A/2)^(A%2*B)
    if used[A]:
        print -1
        break
    used[A] = 1
