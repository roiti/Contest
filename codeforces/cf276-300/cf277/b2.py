m,n = map(int,raw_input().split())
B = [map(int,raw_input().split()) for _ in range(m)]
A = [[1]*n for _ in range(m)]

for r in range(m):
    for c in range(n):
        if B[r][c] == 0:
            for cc in range(n): A[r][cc] = 0
            for rr in range(m): A[rr][c] = 0

fail = False
for r in range(m):
    for c in range(n):
        if B[r][c] == 1:
            if 1 not in A[r] and 1 not in [A[rr][c] for rr in range(m)]:
                fail = True
                break
    if fail: break

if fail: print "NO"
else:
    print "YES"
    for line in A:
        print " ".join(map(str,line))
