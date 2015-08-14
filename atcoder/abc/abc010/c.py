def S(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
 
xa,ya,xb,yb,T,V = map(int,raw_input().split())
n = int(raw_input())
for roop in range(n):
    x,y = map(int,raw_input().split())
    if S(xa,ya,x,y)+S(x,y,xb,yb) <= T*V:
        print "YES"
        break
else:
    print "NO"
