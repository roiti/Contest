from bisect import *
p = [1]*300003
p[0] = p[1] = 0
for i in xrange(2,300003):
    if p[i] and i%7 in (1,6):
        p[2*i::i] = [0]*len(p[2*i::i])
    else:
        p[i] = 0
p = [i for i in xrange(2,300003) if p[i]]

while 1:
    N = int(raw_input())
    if N == 1: break
    ans = [i for i in p[:bisect(p,N+1)] if N%i == 0]
    print "%d: %s"%(N," ".join(map(str,ans)))

