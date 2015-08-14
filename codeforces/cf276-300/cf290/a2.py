n,m = map(int,raw_input().split())
A = [["#"]*m if i%2 == 0 else ["."]*m for i in xrange(n)]
for i in xrange(1,n,2):
    if (i+1)%4 == 0: A[i][0] = "#"
    else: A[i][-1] = "#"
for a in A: print "".join(a)
