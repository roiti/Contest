T = int(raw_input())
for loop in xrange(T):
    x, y, z = map(int, raw_input().split())
    a = (x - y + z) / 2.0
    b = (y - z + x) / 2.0
    c = (z - x + y) / 2.0
    print 2 * (a * b + b * c + c * a)
