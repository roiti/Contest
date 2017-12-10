dxy = zip([1, 1, 0, -1, -1, -1, 0, 1], [0, 1, 1, 1, 0, -1, -1, -1])
H, W = map(int, raw_input().split())    
S = [list(raw_input()) for i in xrange(H)]

for y in xrange(H):
    for x in xrange(W):
        if S[y][x] == "#": continue
        tmp = 0
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < W and 0 <= ny < H): continue
            tmp += 1 if S[ny][nx] == "#" else 0
        S[y][x] = str(tmp)

for s in S:
    print "".join(s)
