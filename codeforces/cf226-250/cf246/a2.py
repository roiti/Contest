n,k = map(int,raw_input().split())
y = map(int,raw_input().split())
ans = 0
for yi in y:
    if yi < 6-k:
        ans += 1
print ans/3
