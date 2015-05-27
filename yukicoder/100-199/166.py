H,W,N,K = map(int,raw_input().split())
if (H*W)%N == K%N:
    print "YES"
else:
    print "NO"