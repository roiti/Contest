n = int(raw_input())
a = map(int,raw_input().split())
ans = 0
for i in a:
    while i%2 == 0 or i%3 == 2:
        i -= 1
        ans += 1
print ans
