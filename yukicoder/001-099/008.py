P = int(raw_input())
for loop in xrange(P):
    N,K = map(int,raw_input().split())
    N -= 1
    while N:
        if N >= K+1:
            N -= K+1
        else:
            print "Win"
            break
    else:
        print "Lose"
