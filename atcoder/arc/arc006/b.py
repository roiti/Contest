N, L = map(int, raw_input().split())
a = [raw_input() for i in xrange(L)]
x = raw_input().index("o")

for h in xrange(L - 1, -1, -1):
    if x > 0 and a[h][x - 1] == "-":
        x -= 2
    if x < 2 * N - 2 and a[h][x + 1] == "-":
        x += 2
print x / 2 + 1
