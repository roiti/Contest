g = sorted("indeednow")
N = int(raw_input())
for loop in xrange(N):
    s = sorted(raw_input())
    print "YES" if s == g else "NO"
