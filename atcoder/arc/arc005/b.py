dxy = {"R":(1, 0), "L":(-1, 0), "U":(0, -1), "D":(0, 1), "RU":(1, -1), "RD":(1, 1), "LU":(-1, -1), "LD":(-1, 1)}

x, y, W = raw_input().split()
x, y = int(x) - 1, int(y) - 1
c = [raw_input() for i in xrange(9)]

dx, dy = dxy[W]
ans = ""
for i in xrange(4):
    ans += c[y][x]
    if not 0 <= x + dx < 9: dx *= -1
    if not 0 <= y + dy < 9: dy *= -1
    x += dx
    y += dy
print ans
