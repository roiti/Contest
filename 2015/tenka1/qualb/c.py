mod = 10 ** 9 + 7
L = int(raw_input())
if L < 9:
    print 0
    exit()

L -= 9
n, k = L / 4, L % 4
ans = (4 * n * (n + 1) / 2 - n) % mod
seq = [n + 1, n, n + 1, n + 1]
for i in xrange(k + 1):
    ans = (ans + seq[i]) % mod

print ans
