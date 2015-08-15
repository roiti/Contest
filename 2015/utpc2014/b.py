x,y = raw_input().split()
x1,x2 = map(int,x.split("."))
y1,y2 = map(int,y.split("."))
if x1 < 0: x2 *= -1
if y1 < 0: y2 *= -1
if (x1,x2,y1,y2) == (0,0,0,0):
    print 1,0,-1,0
    print 0,1,0,-1
    exit()
a,b = x1-1,y1-1
c,d = x2+1000+a,y2+1000+b
print a,b,c,d
a += 1
c,d = x2+a,y2+1000+b
print a,b,c,d
