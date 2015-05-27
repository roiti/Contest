import math
N,K = map(int,raw_input().split())
W = [int(raw_input()) for i in xrange(N)]
mw = 1000001
have = [0]*mw
D = int(math.ceil(mw**0.5))
bucket = [0]*(mw/D+1)
for i in xrange(N):
    p = abs(W[i])/D
    if W[i] > 0:
        cnt = 0
        for j in xrange(p,mw/D+1): cnt += bucket[j]
        for j in xrange(p*D,W[i]): cnt -= have[j]
        if cnt < K:
            have[W[i]] += 1
            bucket[p] += 1
    elif have[-W[i]] > 0:
        have[-W[i]] -= 1
        bucket[p] -= 1
print sum(bucket)