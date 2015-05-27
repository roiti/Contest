n = int(raw_input())
ans = 0
for h in range(1,100000):
    need = h*(h+1)/2
    if n >= need:
        n -= need
        ans += 1
    if n <= 0: break
print ans
