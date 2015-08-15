n,m = map(int,raw_input().split())
p = map(int,raw_input().split())
s = map(int,raw_input().split())
ans = 0
for i in s:
    ans += p[i-1]
print ans
