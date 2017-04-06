import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time
 
sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7
 
def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()
 
 
def main():
    h,w,k,t = LI()
    a = []
    b = []
    for _ in range(k):
        c,d,e,f = LI()
        b.append([c-1,d-1])
        a.append([e-1,f-1])
 
    def ds(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
 
    co = (h//2, w//2)
    ma = []
    for i in range(h):
        for j in range(w):
            if (i+j) % 2 == 0:
                ma.append((i,j))
 
    def mp(a, m):
        b = [[False]*w for _ in range(h)]
        nt = []
 
        for i in range(k):
            ai = a[i]
            b[ai[0]][ai[1]] = i+1
            if (ai[0]+ai[1]) % 2 == 1:
                nt.append(ai)
 
        nt.sort()
 
        for i in range(k):
            mi = m[i]
            if b[mi[0]][mi[1]]:
                continue
            s = list(mi)
            t = nt[0]
            nt = nt[1:]
            while s[0] != t[0] or s[1] != t[1]:
                sn = list(s)
                while True:
                    if sn[0] > t[0]:
                        sn[0] -= 1
                    elif sn[0] < t[0]:
                        sn[0] += 1
                    elif sn[1] < t[1]:
                        sn[1] += 1
                    elif sn[1] > t[1]:
                        sn[1] -= 1
 
                    if b[sn[0]][sn[1]]:
                        break
                b[s[0]][s[1]] = b[sn[0]][sn[1]]
                b[sn[0]][sn[1]] = False
                s = sn
 
        r = [None] * k
        for i in range(h):
            for j in range(w):
                if b[i][j]:
                    r[b[i][j]-1] = (i,j)
        return r
 
 
    def move(a, tr):
        for i in range(k):
            c = tr[i]
            if c == 'U':
                a[i][0] -= 1
            elif c == 'D':
                a[i][0] += 1
            elif c == 'L':
                a[i][1] -= 1
            elif c == 'R':
                a[i][1] += 1
 
    def mp_move(b, ma):
        rr = []
 
        while True:
            mb = mp(b, ma)
            tr = ['-'] * k
            f = [[True]*w for _ in range(h)]
            for bi in b:
                f[bi[0]][bi[1]] = False
 
            mc = 0
 
            for i in range(k):
                bi = b[i]
                mi = mb[i]
 
                if bi[0] > mi[0]:
                    if f[bi[0]-1][bi[1]]:
                        tr[i] = 'U'
                        f[bi[0]-1][bi[1]] = False
                        continue
                elif bi[0] < mi[0]:
                    if f[bi[0]+1][bi[1]]:
                        tr[i] = 'D'
                        f[bi[0]+1][bi[1]] = False
                        continue
 
                if bi[1] > mi[1]:
                    if f[bi[0]][bi[1]-1]:
                        tr[i] = 'L'
                        f[bi[0]][bi[1]-1] = False
                        continue
                elif bi[1] < mi[1]:
                    if f[bi[0]][bi[1]+1]:
                        tr[i] = 'R'
                        f[bi[0]][bi[1]+1] = False
                        continue
 
                mc += 1
 
            if mc == k:
                break
 
            move(b,tr)
            rr.append(tr)
 
        return (b, rr)
 
 
    def mp_mp(b, a):
        rr = []
        aa = list(zip(a, range(k)))
        aa.sort()
 
        for _ in range(200):
            tr = [['-'] * k for _ in range(2)]
            f = [[True]*w for _ in range(h)]
            mc = 0
 
            bis = {}
            for i in range(k):
                bis[tuple(b[i])] = i
 
            for ai, i in aa:
                a0, a1 = ai
                b0, b1 = b[i]
                if b[i] == ai or not f[b0][b1]:
                    mc += 1
                    continue
 
                if b0 > a0 and b1 > a1:
                    if f[b0-1][b1-1] and f[b0-1][b1] and f[b0][b1-1]:
                        nb = bis[(b0-1, b1-1)]
                        if a[nb] > a[i]:
                            f[b0][b1] = f[b0-1][b1-1] = f[b0-1][b1] = f[b0][b1-1] = False
                            tr[0][i] = 'U'
                            tr[1][i] = 'L'
                            tr[0][nb] = 'D'
                            tr[1][nb] = 'R'
                            continue
 
                if b0 > a0 and b1 < a1:
                    if f[b0-1][b1+1] and f[b0-1][b1] and f[b0][b1+1]:
                        nb = bis[(b0-1, b1+1)]
                        if a[nb] > a[i]:
                            f[b0][b1] = f[b0-1][b1+1] = f[b0-1][b1] = f[b0][b1+1] = False
                            tr[0][i] = 'U'
                            tr[1][i] = 'R'
                            tr[0][nb] = 'D'
                            tr[1][nb] = 'L'
                            continue
 
                if b0-1 > a0:
                    if f[b0-2][b1]:
                        if b1 < w-1 and f[b0][b1+1] and f[b0-2][b1+1]:
                            nb1 = bis[(b0-2,b1)]
                            nb2 = bis[(b0-1,b1+1)]
                            if a[nb1] > a[i] and a[nb2] > a[i]:
                                f[b0][b1] = f[b0-1][b1] = f[b0-2][b1] = f[b0][b1+1] = f[b0-1][b1+1] = f[b0-2][b1+1] = False
                                tr[0][i] = 'U'
                                tr[1][i] = 'U'
                                tr[0][nb1] = 'R'
                                tr[1][nb1] = 'D'
                                tr[0][nb2] = 'D'
                                tr[1][nb2] = 'L'
                                continue
 
                        if b1 > 0 and f[b0][b1-1] and f[b0-2][b1-1]:
                            nb1 = bis[(b0-2,b1)]
                            nb2 = bis[(b0-1,b1-1)]
                            if a[nb1] > a[i] and a[nb2] > a[i]:
                                f[b0][b1] = f[b0-1][b1] = f[b0-2][b1] = f[b0][b1-1] = f[b0-1][b1-1] = f[b0-2][b1-1] = False
                                tr[0][i] = 'U'
                                tr[1][i] = 'U'
                                tr[0][nb1] = 'L'
                                tr[1][nb1] = 'D'
                                tr[0][nb2] = 'D'
                                tr[1][nb2] = 'R'
                                continue
 
                if b1-1 > a1:
                    if f[b0][b1-2]:
                        if b0 == h-1 and f[b0-1][b1] and f[b0-1][b1-2]:
                            nb1 = bis[(b0,b1-2)]
                            nb2 = bis[(b0-1,b1-1)]
                            f[b0][b1] = f[b0][b1-1] = f[b0][b1-2] = f[b0-1][b1] = f[b0-1][b1-1] = f[b0-1][b1-2] = False
                            tr[0][i] = 'L'
                            tr[1][i] = 'L'
                            tr[0][nb1] = 'U'
                            tr[1][nb1] = 'R'
                            tr[0][nb2] = 'R'
                            tr[1][nb2] = 'D'
                            continue
 
                        if b0 < h-1 and f[b0+1][b1] and f[b0+1][b1-2]:
                            nb1 = bis[(b0,b1-2)]
                            nb2 = bis[(b0+1,b1-1)]
                            f[b0][b1] = f[b0][b1-1] = f[b0][b1-2] = f[b0+1][b1] = f[b0+1][b1-1] = f[b0+1][b1-2] = False
                            tr[0][i] = 'L'
                            tr[1][i] = 'L'
                            tr[0][nb1] = 'D'
                            tr[1][nb1] = 'R'
                            tr[0][nb2] = 'R'
                            tr[1][nb2] = 'U'
                            continue
 
                if b1+1 < a1:
                    if f[b0][b1+2]:
                        if b0 == h-1 and f[b0-1][b1] and f[b0-1][b1+2]:
                            nb1 = bis[(b0,b1+2)]
                            nb2 = bis[(b0-1,b1+1)]
                            f[b0][b1] = f[b0][b1+1] = f[b0][b1+2] = f[b0-1][b1] = f[b0-1][b1+1] = f[b0-1][b1+2] = False
                            tr[0][i] = 'R'
                            tr[1][i] = 'R'
                            tr[0][nb1] = 'U'
                            tr[1][nb1] = 'L'
                            tr[0][nb2] = 'L'
                            tr[1][nb2] = 'D'
                            continue
 
                        if b0 < h-1 and f[b0+1][b1] and f[b0+1][b1+2]:
                            nb1 = bis[(b0,b1+2)]
                            nb2 = bis[(b0+1,b1+1)]
                            f[b0][b1] = f[b0][b1+1] = f[b0][b1+2] = f[b0+1][b1] = f[b0+1][b1+1] = f[b0+1][b1+2] = False
                            tr[0][i] = 'R'
                            tr[1][i] = 'R'
                            tr[0][nb1] = 'D'
                            tr[1][nb1] = 'L'
                            tr[0][nb2] = 'L'
                            tr[1][nb2] = 'U'
                            continue
 
 
                mc += 1
 
            if mc == k:
                break
 
            move(b,tr[0])
            for i in range(k):
                for j in range(i+1, k):
                    if b[i] == b[j]:
                        print('error', i,j,b[i], tr[0][i], tr[0][j])
            move(b,tr[1])
            rr.append(tr[0])
            rr.append(tr[1])
 
 
        return rr
 
 
    def r_rr(rr):
        r = []
        for tr in rr:
            t = ''
            for c in tr:
                if c == 'U':
                    t += 'D'
                elif c == 'D':
                    t += 'U'
                elif c == 'L':
                    t += 'R'
                elif c == 'R':
                    t += 'L'
                else:
                    t += '-'
            r.append(t)
        r.reverse()
        return r
 
    b, br = mp_move(b, ma)
    a, ar = mp_move(a, ma)
    mr = mp_mp(b, a)
    rr = br + mr + r_rr(ar)
 
    print(len(rr))
    for c in rr:
        print(''.join(c))
 
 
 
main()
