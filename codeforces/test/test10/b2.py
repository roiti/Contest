n = input()
a = map(int,raw_input().split())
m = sum(a)/n
res = 0
for i in range(n-1):
    d = m - a[i]
    a[i] += d
    a[i+1] -= d
    res += abs(d)
print res
