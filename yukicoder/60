N,K = map(int,raw_input().split())
M = [[0]*1010 for i in xrange(1010)]
for loop in xrange(N):
    x,y,hp = map(int,raw_input().split())
    x += 500; y += 500
    M[y][x] = hp

A = [[0]*1010 for i in xrange(1010)]
for loop in xrange(K):
    ax,ay,w,h,d = map(int,raw_input().split())
    ax += 500; ay += 500
    ex,ey = min(1009,ax+w+1), min(1009,ay+h+1)
    A[ay][ax] += d
    A[ay][ex] -= d
    A[ey][ax] -= d
    A[ey][ex] += d
        
ans = 0
for x in xrange(1010):
    for y in xrange(1,1010):
        A[y][x] += A[y-1][x]
for y in xrange(1010):
    for x in xrange(1010):
        if x > 0: A[y][x] += A[y][x-1]
        ans += max(0, M[y][x]-A[y][x])
print ans
