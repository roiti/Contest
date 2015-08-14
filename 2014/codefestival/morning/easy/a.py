n = input()
a = map(int,raw_input().split())
ans = 0
for i in range(n-1):
    ans += a[i+1]-a[i]
print ans*1.0/(n-1)
