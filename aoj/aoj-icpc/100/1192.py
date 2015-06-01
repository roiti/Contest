def tax(a,p):
    return int(a * (1.0 + p))
    
while 1:
    x,y,s = map(int,raw_input().split())
    if x == y == s == 0: break
    x /= 100.0-1e-10
    y /= 100.0-1e-10

    ans = 0
    for a in xrange(1,s):
        b = s - tax(a,x)
        while tax(a,x) + tax(b,x) > s: b -= 1
        if (b < 1 or s-1 < b) or tax(a,x) + tax(b,x) != s: continue
        ans = max(ans, tax(a,y) + tax(b,y))
    print ans        


