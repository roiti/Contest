size = 20
def dist(ax, ay, bx, by):
    return (ax - bx) ** 2 + (ay - by) ** 2

def check(x, y):
    for dy in xrange(-1, 2):
        for dx in xrange(-1, 2):
            bx, by = x / size + dx, y / size + dy
            if 0 <= bx < 20000 / size + 1 and 0 <= by < 20000 / size + 1:
                for cx, cy in block[by][bx]:
                    if dist(x, y, cx, cy) < 400:
                        return False
    return True
    
N = int(raw_input())
block = [[[] for i in xrange(20000 / size + 1)] for j in xrange(20000 / size + 1)]

ans = 0
for loop in xrange(N):
    x, y = map(int, raw_input().split())
    if check(x, y):
        ans += 1
        block[y / size][x / size].append((x, y))
print ans