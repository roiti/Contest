N = int(raw_input())
ans = 0
for loop in xrange(N):
    a,b,c,d,e = map(int,raw_input().split())
    ans = max(ans, a+b+c+d+e*110./900.)
print "%.6f"%ans
n = input()
print n*(n+1)/2
