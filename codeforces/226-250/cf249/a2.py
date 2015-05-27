n,m = map(int,raw_input().split())
a = map(int,raw_input().split())
i = 0
count = 1
cur = 0
while sum(a) > 0:
    if cur + a[i] <= m:
        cur += a[i]
        a[i] = 0
        i = (i+1)%n
    else:
        count += 1
        cur = 0
print count
