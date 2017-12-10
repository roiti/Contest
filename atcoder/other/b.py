def convert(s, to, frm):
    dic = dict(zip(to, frm))
    res = "".join(dic[si] for si in s)
    return res

alpha = "abcdefghijklmnopqrstuvwxyz"
N = int(raw_input())
S = [raw_input() for i in xrange(N)]

Q = int(raw_input())
for loop in xrange(Q):
    A, B, C = raw_input().split()
    A, B = int(A) - 1, int(B) - 1
    for i in xrange(A, B + 1):
        S[i] = convert(S[i], C, alpha)
    S[A:B + 1] = sorted(S[A:B + 1])
    for i in xrange(A, B + 1):
        S[i] = convert(S[i], alpha, C)
for s in S:
    print s
