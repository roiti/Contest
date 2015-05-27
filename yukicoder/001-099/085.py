N,M,C = map(int,raw_input().split())
if min(N,M) == 1: print "YES" if max(N,M) == 2 else "NO"
else: print "YES" if N*M%2 == 0 else "NO"