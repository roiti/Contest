T = int(raw_input())
for loop in xrange(T):
    n = int(raw_input())
    d = map(int, raw_input().split())
    print len(set(d))
