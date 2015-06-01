while 1:
    H = int(raw_input())
    if H == 0: break
    A = [map(int,raw_input().split())+[0] for _ in range(H)]
    ans = 0
    while 1:
        vanish = False
        for h in range(H):
            l = r = 0
            while r < 6:
                if A[h][r] != A[h][l]:
                    if r-l >= 3:
                        if A[h][l] == 0:break
                        ans += A[h][l]*(r-l)
                        A[h][l:r] = [0]*(r-l)
                        vanish = True
                    l = r
                r += 1
        if not vanish: break
        for h in range(H)[::-1]:
            for w in range(5):
                if A[h][w] == 0:
                    for hh in range(h)[::-1]:
                        if A[hh][w] != 0:
                            A[h][w] = A[hh][w]
                            A[hh][w] = 0
                            break
    print ans

