N = int(raw_input())
a = map(int,raw_input().split())
ans = 0
for i in range(N-2):
    if len(set(a[i:i+3])) == 3 and a[i+1] != sorted(a[i:i+3])[1]:
        ans += 1
print ans
