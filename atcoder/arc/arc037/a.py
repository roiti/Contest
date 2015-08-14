N = int(raw_input())
m = map(int,raw_input().split())
print sum(max(0, 80-m[i]) for i in xrange(N))
