import sys

def puts(s):
    print s
    sys.stdout.flush()

N = int(raw_input())

win = [0] * N
even = 1 - N % 2
M = N - even
circle = [[i + 1, M - i - 1] for i in xrange((N - 1) / 2)]
for i in xrange(M):
    pair = [[(p + i) % M + 1, (q + i) % M + 1] for p, q in circle]
    if even:
        pair += [[i + 1, N]]
    pair += [[0, 0] for i in xrange(N - len(pair))]
    query = "? " + " ".join(" ".join(map(str, p)) for p in pair)

    puts(query)

    reply = raw_input().split()
    for i, s in enumerate(reply):
        p, q = pair[i]
        if s == ">": win[p - 1] += 1
        if s == "<": win[q - 1] += 1

ans = [0] * N
for i, r in enumerate(win, 1):
    ans[r] = i

puts("! " + " ".join(map(str, ans)))
