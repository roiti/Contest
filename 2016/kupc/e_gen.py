import random
H, W = map(int, raw_input().split())
a = "......................X"
print H, W
print "."*W
for y in xrange(H - 2):
    s = "." + "".join([a[random.randint(0,len(a) - 1)] for i in xrange(W - 2)]) + "."
    print s
print "."*W
