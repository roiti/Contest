n = int(raw_input())
fs = [raw_input().split() for i in xrange(n)]
p = map(int,raw_input().split())

fs = [fs[pi-1] for pi in p]
handle = min(fs[0])
for i in xrange(1,n):
    if fs[i][0] > handle and fs[i][1] > handle:
        handle = min(fs[i])
    elif fs[i][0] > handle:
        handle = fs[i][0]
    elif fs[i][1] > handle:
        handle = fs[i][1]
    else:
        print "NO"
        break
else:
    print "YES"
