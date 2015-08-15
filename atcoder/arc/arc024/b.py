N = int(raw_input())
c = [int(raw_input()) for i in xrange(N)]
if len(set(c)) == 1:
    print -1
else:
    ans = 1
    c += c
    seq = 1
    for i in xrange(2 * N - 1):
        if c[i] == c[i + 1]:
            seq += 1
        else:
            ans = max(ans, (seq + 1) / 2)
            seq = 1
    print max(ans, (seq + 1) / 2)
