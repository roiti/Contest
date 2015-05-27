N,K = map(int,raw_input().split())
R = N+2
p = [1]*R
c = [0]*R
p[0] = p[1] = 0
for i in xrange(2,R):
    if p[i]:
        p[2*i::i] = [0]*len(p[2*i::i])
        c[2*i::i] = [j+1 for j in c[2*i::i]]
c = [c[i]+p[i] for i in xrange(R)]
print sum(c[i] >= K for i in xrange(2,N+1))