W, H, N = map(int, raw_input().split())
xya = [map(int, raw_input().split()) for i in xrange(N)]
lx, hx = 0, W
ly, hy = 0, H
for x, y, a in xya:
    if a == 1: lx = max(lx, x)
    if a == 2: hx = min(hx, x) 
    if a == 3: ly = max(ly, y) 
    if a == 4: hy = min(hy, y) 
print max(0, hx - lx)*max(0, hy - ly)
