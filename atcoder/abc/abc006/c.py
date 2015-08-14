N,M = map(int,raw_input().split())
for c in xrange(1000000):
    b = M-2*N-2*c
    if b < 0:
        print -1,-1,-1
        break
    if N-b-c >= 0:
        print N-b-c,b,c
        break
