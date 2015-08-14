from collections import defaultdict
R, C, K = map(int, raw_input().split())
N = int(raw_input())
row, col = [0] * R, [0] * C
rc = defaultdict(set)
for loop in xrange(N):
    r, c = map(int, raw_input().split())
    r -= 1; c -= 1
    row[r] += 1
    col[c] += 1
    rc[r].add(c)
 
nc = defaultdict(set)
for i in xrange(C):
    nc[col[i]].add(i)
 
ans = 0
for r in xrange(R):
    k = K - row[r]
    if k < 0: continue
    ans += len(nc[k] - rc[r])
    ans += len(nc[k+1] & rc[r])
 
print ans
