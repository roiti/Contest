def gcd(a,b):
    while b: a,b = b,a%b
    return a
    
n,x0,y0 = map(int,raw_input().split())
xy = [map(int,raw_input().split()) for i in xrange(n)]
xy = [[x-x0,y-y0] for x,y in xy]
xy = set((x/gcd(x,y),y/gcd(x,y)) for x,y in xy)
print len(xy)
