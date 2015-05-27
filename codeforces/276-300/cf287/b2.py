r,x0,y0,x1,y1 = map(int,raw_input().split())
d = ((x0-x1)**2+(y0-y1)**2)**0.5
cnt = 0
while d >= 2*r:
    d -= 2*r
    cnt += 1
print cnt if d == 0 else cnt+1
