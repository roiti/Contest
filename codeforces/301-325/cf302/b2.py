n, k = map(int, raw_input().split())
A = [["S"] * n for i in xrange(n)]

for y in xrange(n):
    for x in xrange(y % 2, n, 2):
        if k == 0: break
        A[y][x] = "L"
        k -= 1
    
if k == 0:
    print "YES"
    for line in A:
        print "".join(line)
else:
    print "NO"
