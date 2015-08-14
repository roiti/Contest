N = int(raw_input())
a = map(int,raw_input().split())
for i in xrange(N):
    while a[i]%2 == 0: a[i] /= 2
print len(set(a))
