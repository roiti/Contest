import math
def dist(x, y):
    return (x - gx) ** 2 + (y - gy) ** 2
    
N = int(raw_input())
 
A = [map(float, raw_input().split()) for i in xrange(N)]
gx = sum(x for x, y in A) / N
gy = sum(y for x, y in A) / N
maxDistA = 0.0
for x, y in A:
    maxDistA = max(maxDistA, dist(x, y))
    
B = [map(float, raw_input().split()) for i in xrange(N)]
gx = sum(x for x, y in B) / N
gy = sum(y for x, y in B) / N
maxDistB = 0.0
for x, y in B:
    maxDistB = max(maxDistB, dist(x, y))
 
print "%.10f" % (math.sqrt(maxDistB / maxDistA))
