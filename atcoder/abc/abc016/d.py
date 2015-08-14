# coding: utf-8
def denomi(cx,cy,dx,dy):
    return (by-ay)*(dx-cx)-(bx-ax)*(dy-cy)
    
def getip(cx,cy,dx,dy):
    dn = denomi(cx,cy,dx,dy)*1.0
    x = ((cy*dx-cx*dy)*(bx-ax)-(ay*bx-ax*by)*(dx-cx))/dn
    y = ((cy*dx-cx*dy)*(by-ay)-(ay*bx-ax*by)*(dy-cy))/dn
    return x,y
 
def ison(x,y):
    if min(cx,dx) <= x <= max(cx,dx) and min(cy,dy) <= y <= max(cy,dy):
            if min(ax,bx) <= x <= max(ax,bx) and min(ay,by) <= y <= max(ay,by):
                return True
    return False
    
ax,ay,bx,by = map(int,raw_input().split())
n = int(raw_input())
xy = [map(int,raw_input().split()) for _ in range(n)]
num = 0
for c,d in zip(xy,xy[1:]+[xy[0]]):
    cx,cy = c
    dx,dy = d
    if denomi(cx,cy,dx,dy) != 0:
        x,y = getip(cx,cy,dx,dy)
        if ison(x,y):
            num += 1
print num/2+1
