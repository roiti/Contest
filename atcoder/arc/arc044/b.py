mod = 10 ** 9 + 7
N = int(raw_input())
A = map(int, raw_input().split())

if A[0] != 0 or A.count(0) > 1:
    print 0
    exit()

cnt = [0] * N
for ai in A:
    cnt[ai] += 1

ans = 1
for i in xrange(1, N):
    if cnt[i] > 0:
        if cnt[i - 1] == 0:
            ans = 0
            break
        ans = ans * pow(pow(2, cnt[i - 1], mod) - 1, cnt[i],  mod) % mod
        ans = ans * pow(2, cnt[i] * (cnt[i] - 1) / 2, mod) % mod
print ans
