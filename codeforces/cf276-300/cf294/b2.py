n = int(raw_input())
a = sorted(map(int,raw_input().split()))
b = sorted(map(int,raw_input().split()))
c = sorted(map(int,raw_input().split()))

for i in xrange(n-1):
    if a[i] != b[i]:
        print a[i]
        break
else:
    print a[-1]
for i in xrange(n-2):
    if b[i] != c[i]:
        print b[i]
        break
else:
    print b[-1]
