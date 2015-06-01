N,W,H = map(int,raw_input().split())
X,Y = [0]*(W+1),[0]*(H+1)
for loop in xrange(N):
    x,y,w = map(int,raw_input().split())
    X[max(0,x-w)] += 1
    X[min(W,x+w)] += -1
    Y[max(0,y-w)] += 1
    Y[min(H,y+w)] += -1
for i in xrange(1,W+1): X[i] += X[i-1]
for i in xrange(1,H+1): Y[i] += Y[i-1]
print "Yes" if min(X[:-1]) > 0 or min(Y[:-1]) > 0 else "No"

