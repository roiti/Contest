L, R = map(int, raw_input().split())
size = [0] * 31
l = map(int, raw_input().split())
r = map(int, raw_input().split())
ans = 0
for li in l:
    size[li - 10] += 1
for ri in r:
    if size[ri - 10] > 0:
        size[ri - 10] -= 1
        ans += 1
print ans
