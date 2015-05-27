B = int(raw_input())
N = int(raw_input())
C = [int(raw_input()) for i in xrange(N)]

ans = 10**18
l, r = -1, 10**18
while r - l > 2:
    lm, rm = (2 * l + r) / 3, (l + 2 * r) / 3
    if   sum(lm - c for c in C) > B:
        r = lm
    elif sum(rm - c for c in C) > B:
        r = rm
    elif sum(abs(lm - c) for c in C) <= sum(abs(rm - c) for c in C):
        r = rm
    else:
        l = lm

print sum(abs((r + l) / 2 - c) for c in C)