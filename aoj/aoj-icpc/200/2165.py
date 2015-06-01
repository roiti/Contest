import math
M = 256
while 1:
    N = int(raw_input())
    if N == 0: break
    H = 1e10
    I = map(int,raw_input().split())
    for S in range(16):
        for A in range(16):
            for C in range(16):
                R = S
                O = [0]*M
                for i in I:
                    R = (A*R+C)%M
                    O[(i+R)%M] += 1
                tmp = -sum(1.0*x/N*math.log(1.0*x/N,2) for x in O if x > 0)
                if tmp < H:
                    H = tmp
                    ans = [S,A,C]
    print " ".join(map(str,ans))

