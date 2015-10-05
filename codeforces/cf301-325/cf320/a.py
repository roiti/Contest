_a, b = map(int, raw_input().split())
a = _a
if a < b:
    print -1
    exit()

x = (a + b) / 2.0
if x < a:
    a = 2 * x - a

x /= int(x / a)
print "%.10f" % x
