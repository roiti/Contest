import sys
N = int(raw_input())
mxdist = 0
for i in xrange(2,N+1):
    print "? %d %d"%(1,i)
    sys.stdout.flush()
    dist = int(raw_input())
    if dist > mxdist:
        mxdist = dist
        v = i
 
ans = mxdist
for i in xrange(2,N+1):
    if i == v: continue
    print "? %d %d"%(v,i)
    sys.stdout.flush()
    dist = int(raw_input())
    ans = max(ans,dist)
 
print "! %d"%ans
exit()
