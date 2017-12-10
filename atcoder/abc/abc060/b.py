A, B, C = map(int, raw_input().split()) 
for i in xrange(1, 1000):
    if A*i%B == C:
        print "YES"
        exit()
print "NO"
