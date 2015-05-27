N = int(raw_input())
ab = [map(int,raw_input().split()) for i in xrange(N)]

for i in xrange(N):
    w1 = ab[i][0] + 4*ab[i][1]
    for j in xrange(i+1,N):
        w2 = ab[j][0] + 4*ab[j][1]
        if abs(w1-w2) % 2 != 0:
            print -1
            exit()

mx = max(a+4*b for a,b in ab)    
ans = 0
for a,b in ab:
    ans += (mx-(a + 4*b))/2
print ans