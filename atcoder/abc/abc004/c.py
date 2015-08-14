C = [1,2,3,4,5,6]
N = int(raw_input())%30
for i in xrange(N):
    a,b = i%5,i%5+1
    C[a],C[b] = C[b],C[a]
print "".join(map(str,C))
