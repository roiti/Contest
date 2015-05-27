import bisect
N = int(raw_input())
A = int(raw_input())
B = sorted(map(int, raw_input().split()))
C = int(raw_input())
D = sorted(map(int, raw_input().split()))

ans = 0
b = B[:]
d = D[:]
for i in xrange(N):
    if i % A == 0: b = B[:]
    if i % C == 0: d = D[:]
    if max(b) <= min(d):
        b.pop(0)
        d.pop()
        continue
    for j in xrange(len(b)):
        pos = bisect.bisect_left(d, b[j])
        if pos > 0:
            b.pop(j)
            d.pop(pos - 1)
            break
    ans += 1
print ans