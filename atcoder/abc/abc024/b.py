N, T = map(int, raw_input().split())
op = [0] * 2000000
for i in xrange(N):
    a = int(raw_input())
    op[a] += 1
    op[a + T] -= 1
ans = 0
for i in xrange(1, 2000000):
    op[i] += op[i - 1]
    if op[i] > 0 :ans += 1
print ans
