p,q = map(float,raw_input().split())
a = [[0.]*2 for i in xrange(3)]
a[0][0] = p
a[0][1] = 1-p
for i in xrange(1,3):
    a[i][0] = a[i-1][1]
    a[i][1] = (1-q)*a[i-1][0]
print "YES" if a[1][0] < a[2][0] else "NO"
