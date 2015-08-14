n = int(raw_input())
a = sorted(map(int,raw_input().split()))
m = int(raw_input())
b = sorted(map(int,raw_input().split()))
ans = i = j = 0
while 1:
    if abs(a[i]-b[j]) <= 1:
        ans += 1
        if i == n-1 or j == m-1:break
        i += 1
        j += 1
    elif a[i]-b[j] > 1:
        if j == m-1: break
        j += 1
    elif a[i]-b[j] < -1:
        if i == n-1:break
        i += 1
print ans
