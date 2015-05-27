h,n = map(int,raw_input().split())
n -= 1
way = ""
for loop in range(h):
    way = "L"+way if n%2 == 0 else "R"+way
    n /= 2

ans = 1 if way[0] == "L" else 2**h
for i in range(1,h):
    if way[i] != way[i-1]:
        ans += 1
    else:
        ans += 2**(h-i)
print ans
