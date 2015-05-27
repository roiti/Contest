def gcd(a,b):
    if min(a,b) == 0: return max(a,b)
    while b: a,b = b,a%b
    return a
    
Q = int(raw_input())
for loop in xrange(Q):
    W,H,D,Mx,My,Hx,Hy,Vx,Vy = map(int,raw_input().split())
    d = gcd(abs(Vx),abs(Vy))
    D *= d; Vx /= d; Vy /= d;
    
    x,y = Hx,Hy
    xy = [[0]*(W+1) for i in xrange(H+1)]
    count = set([])
    for t in xrange(D):
        x += Vx; y += Vy
        while not (0 <= x <= W):
            x = -x if x < 0 else 2*W-x
            Vx = -Vx
        while not (0 <= y <= H):
            y = -y if y < 0 else 2*H-y
            Vy = -Vy
        if xy[y][x] > 4: break
        xy[y][x] += 1
    print "Hit" if xy[My][Mx] else "Miss"
