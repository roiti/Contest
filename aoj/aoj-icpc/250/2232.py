import copy

def can_empty(A,y,x):
    A[y][x],A[y][x+1] = A[y][x+1],A[y][x]
    num = sum(W-a.count(".") for a in A)
    while 1:
        # Fall processing
        for w in xrange(W):
            seq = ("".join(A[h][w] for h in xrange(H))).replace(".","")
            seq += "."*(H-len(seq))
            for h in xrange(H):
                A[h][w] = seq[h]

        # Banish processing
        B = [[0]*W for _ in xrange(H)]
        for h in xrange(H):
            cnt = 1
            for w in xrange(1,W):
                if A[h][w] == A[h][w-1]: cnt += 1
                else:
                    if cnt >= n and A[h][w-1] != ".":
                        for wi in xrange(w-cnt,w): B[h][wi] = 1
                    cnt = 1
            if cnt >= n and A[h][W-1] != ".":
                for wi in xrange(W-cnt,W): B[h][wi] = 1
        for w in xrange(W):
            cnt = 1
            for h in xrange(1,H):
                if A[h][w] == A[h-1][w]: cnt += 1
                else:
                    if cnt >= n and A[h-1][w] != ".":
                        for hi in xrange(h-cnt,h): B[hi][w] = 1
                    cnt = 1
            if cnt >= n and A[H-1][w] != ".":
                for hi in xrange(H-cnt,H): B[hi][w] = 1

        banish = False
        for h in xrange(H):
            for w in xrange(W):
                if B[h][w]:
                    A[h][w] = "."
                    num -= 1
                    banish = True
        if not banish: return False
        if num == 0: return True
        

# Entry point
H,W,n = map(int,raw_input().split())
A = [list(raw_input()) for _ in xrange(H)][::-1]

ans = False
for h in xrange(H):
    for w in xrange(W-1):
        if A[h][w] == A[h][w+1]: continue
        if can_empty(copy.deepcopy(A),h,w):
            ans = True
            break
    if ans: break
print "YES" if ans else "NO"

