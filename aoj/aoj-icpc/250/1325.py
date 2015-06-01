C = set([i*i+j*j for i in xrange(160) for j in xrange(160)])

N = int(raw_input())
for loop in xrange(N):
    p,q = map(abs,map(int,raw_input().split()))
    pq = p*p+q*q

    cnt = 0
    for x in xrange(0,max(p,q)):
        for y in xrange(x,max(p,q)):
            xy = x*x+y*y
            if xy < 1: continue
            if pq%xy == 0 and pq/xy in C:
                cnt += 1
    print "P" if cnt == 1 else "C"

