a = [map(int, raw_input().split()) for i in xrange(4)]

for i in xrange(16):
    for y in xrange(4):
        for x in xrange(4):
            if a[y][x] == 0:
                x0, y0 = x, y
            if a[y][x] - 1 == i:
                diff = abs(i % 4 - x) + abs(i / 4 - y)
                if diff > 1:
                    print "No"
                    exit()
inv = 0
a[y0][x0] = 16
for i in xrange(16):
    for j in xrange(i + 1, 16):
        if a[i/4][i%4] > a[j/4][j%4]: inv += 1

if (3 - x0 + 3 - y0 + inv) % 2 == 0:
    print "Yes"
else:
    print "No"

