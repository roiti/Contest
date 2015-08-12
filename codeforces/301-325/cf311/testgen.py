n = 100000
l = [i / 2 + 1 for i in xrange(n)]
d = [i / 100 + 1 for i in xrange(n)]
print n
print " ".join(map(str, l))
print " ".join(map(str, d))


