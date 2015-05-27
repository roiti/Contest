n, m, q = map(int, raw_input().split())
A = [map(int, raw_input().split()) for i in xrange(n)]

score = [0] * n
for r in xrange(n):
    seq = 0
    for c in xrange(m):
        if A[r][c] == 1:
            seq += 1
            score[r] = max(score[r], seq)
        else:
            seq = 0
ans = max(score)

for loop in xrange(q):
    i, j = map(int, raw_input().split())
    i -= 1; j -= 1
    A[i][j] = 1 - A[i][j]

    bef = score[i]
    score[i] = 0
    seq = 0
    for c in xrange(m):
        if A[i][c] == 1:
            seq += 1
            score[i] = max(score[i], seq)
        else:
            seq = 0

    print max(score)
