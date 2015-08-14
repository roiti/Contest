ans = 0
for loop in range(3):
    s,e = map(int,raw_input().split())
    ans += s*e/10
print ans
