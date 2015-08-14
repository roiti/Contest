alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
S1,S2,S3 = raw_input(),raw_input(),raw_input()
r1 = r2 = len(S1)/2
N1,N2,N3 = [S1.count(i) for i in alpha],[S2.count(i) for i in alpha],[S3.count(i) for i in alpha]
for i in range(len(alpha)):
    N1[i] = min(N1[i],N3[i])
    N2[i] = min(N2[i],N3[i])
    for i in range(len(alpha)):
        if N3[i] > N1[i]+N2[i]:
            print "NO"
        break
    if N3[i] == N1[i]+N2[i]:
        r1 -= N1[i]
        r2 -= N2[i]
        N3[i] = 0
    elif N1[i] == 0 and N3[i] <= N2[i]:
        r2 -= N3[i]
        N3[i] = 0
    elif N2[i] == 0 and N3[i] <= N1[i]:
        r1 -= N3[i]
        N3[i] = 0
else:
    if sum(N1) >= r1 >= 0 and sum(N2) >= r2 >= 0:
        print "YES"
    else:
        print "NO"
