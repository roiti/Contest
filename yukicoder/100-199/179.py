H, W = map(int, raw_input().split())
S = [list(raw_input()) for i in xrange(H)]

black = 0
for y in xrange(H):
    for x in xrange(W):
        if S[y][x] == "#": black += 1
if black == 0 or black % 2 == 1:
    print "NO"
    exit()
    
for dy in xrange(H):
    for dx in xrange(-W, W):
        if abs(dx) + dy == 0: continue

        flag = True
        used = [[S[y][x] == "." for x in xrange(W)] for y in xrange(H)] 

        for y in xrange(H-dy):
            for x in xrange(W):
                if used[y][x]: continue
                if not (0 <= x+dx < W) or used[y+dy][x+dx]:
                    flag = False
                    break
                used[y][x] = used[y+dy][x+dx] = True
            if not flag: break
        else:
            if sum(map(sum, used)) != H*W: continue
            print "YES"
            exit()

print "NO"
