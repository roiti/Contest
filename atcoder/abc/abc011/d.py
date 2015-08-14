fact = {i:0 for i in range(1001)}
def f(n):
    res,nn = 1,n
    while n > 0:
        if fact[n] > 0:
            res *= fact[n]
            return res
        res *= n
        n -= 1
    fact[nn] = res
    return res
 
N,D = map(int,raw_input().split())
X,Y = map(int,raw_input().split())
ans = 0
for px in xrange(N+1):
    if px*D-X < 0 or (px*D-X)%D != 0: continue
    dx = (px*D-X)/D
    for py in xrange(N-px-dx+1):
        if py*D-Y < 0 or (py*D-Y)%D != 0: continue
        dy = (py*D-Y)/D
        if px+dx+py+dy == N:
            ans += f(N)/f(px)/f(dx)/f(py)/f(dy)
 
for i in range(N):
    if len(str(ans)) > 14: ans /= 4
    else: ans /= 4.0
print "%.15f"%ans
