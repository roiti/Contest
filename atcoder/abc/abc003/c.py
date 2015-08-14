N,K = map(int,raw_input().split())
R = sorted(map(int,raw_input().split()))
rate = 0
for i in xrange(N-K,N):
    rate = (rate+R[i])/2.0
print rate
