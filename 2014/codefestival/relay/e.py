h, w = map(int, raw_input().split())
b = [raw_input() for i in xrange(h)]
ans = 0
for y in xrange(h):
    for x in xrange(w):
        if b[y][x] != ".": ans += int(b[y][x])
print ans
