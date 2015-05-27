N,L = map(int,raw_input().split())
t = l = 0
for loop in range(N):
    X,W,T = map(int,raw_input().split())
    t += X-l
    if t/T%2 == 0:
            if (t+W-1)/T-t/T > 0:
                    t += (T-t%T)+T
    else:
        t += T-t%T
    t += W
    l = X+W
print t+L-l