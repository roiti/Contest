N = int(raw_input())
L = map(int,raw_input().split())
K = int(raw_input())
ans = 10**4
d,u = 0,10**9
for loop in xrange(50):
    cnt = sum(int(l/ans) for l in L)
    if cnt < K: u = ans
    else: d = ans
    ans = (u+d)/2.
print "%.10f"%ans