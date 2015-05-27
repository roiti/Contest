W,H,C = raw_input().split()
W,H = int(W),int(H)
C += "B" if C == "W" else "W"
A = C*(W/2+1)
for h in range(H):
    print "".join(A[h%2:W+h%2])