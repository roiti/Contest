N = int(raw_input())
a = [int(raw_input()) for i in xrange(N)]
i = 0
ans = 0
while True:
    if a[i] == -1:
        break
    ni = a[i] - 1
    a[i] = -1
    i = ni
    ans += 1
    if i == 1:
        break
print ans if a[i] != -1 else -1

