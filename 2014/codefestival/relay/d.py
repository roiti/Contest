n = int(raw_input())
B = [raw_input() for i in xrange(n)]
X = Y = 0
for y in xrange(n):
    for x in xrange(n):
        if B[y][x] == "X":
            X += y
        if B[y][x] == "Y":
            Y += n - 1 - y
if X == Y:
    print "Impossible"
else:
    print "X" if X > Y else "Y"
