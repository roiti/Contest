ans = [0] * (10 ** 5 + 2)
for i in xrange(1, 10 ** 5 + 2):
    b = bin(i)[2:]
    cnt = 0
    for j in xrange(len(b) - 2):
        if b[j:j + 3] == "101":
            cnt += 1
    ans[i] = cnt

T = int(raw_input())
for loop in xrange(T):
    R, K = map(int, raw_input().split())
    print sum(1 for i in xrange(1, R + 1) if ans[i] >= K)
