N, M, A, B = map(int, raw_input().split())
for i in xrange(M):
    if N <= A: N += B
    c = int(raw_input())
    N -= c
    if N < 0:
        print i + 1
        break
else:
    print "complete"
    
