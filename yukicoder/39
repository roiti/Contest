a = raw_input()
ans = int(a)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        ans = max(ans, int(a[:i]+a[j]+a[i+1:j]+a[i]+a[j+1:]))
print ans
