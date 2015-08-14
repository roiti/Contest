n,m = map(int,raw_input().split())
hb = [0]*n
hg = [0]*m
for i in map(int,raw_input().split())[1:]: hb[i] = 1
for i in map(int,raw_input().split())[1:]: hg[i] = 1

for i in xrange(1000000):
    hb[i%n] = hg[i%m] = max(hb[i%n],hg[i%m])
print "Yes" if min(hb+hg) > 0 else "No"
