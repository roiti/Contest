T = int(raw_input())
for loop in xrange(T):
    N = int(raw_input())
    L = map(int,raw_input().split())
    L = sorted([[L.count(i),i] for i in set(L)])[::-1]
    ans = 0
    while len(L) >= 3:
        for i in range(3)[::-1]:
            L[i][0] -= 1
            if L[i][0] == 0:
                L.pop(i)
        L = sorted(L)[::-1]
        ans += 1
    print ans