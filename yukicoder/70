N = int(raw_input())
ans = 0
for loop in xrange(N):
    H,M,h,m = map(int,raw_input().replace(":"," ").split())
    a,b = 60*H+M,60*h+m
    ans += b-a+1440*(a>b)
print ans