N = int(raw_input())
K = int(raw_input())
d1 = [[0]*61 for _ in range(10)]
d2 = [[0]*61 for _ in range(10)]
for i in range(N):
    if i == 0:
        d1[0][1:7] = [1]*6
        if N-K > 0: d2[0][1:7] = [1]*6
        else:       d2[0][4:7] = [1]*3
        continue
    for j in range(2,61):
        d1[i][j] += sum(d1[i-1][k] for k in range(max(0,j-6),j))
        if i < N-K: d2[i][j] += sum(d2[i-1][k] for k in range(max(0,j-6),j))
        else:       d2[i][j] += sum(d2[i-1][k] for k in range(max(0,j-6),max(0,j-3)))

sum1 = sum(d1[N-1])
sum2 = sum(d2[N-1])
ans = sum(1.0*d2[N-1][i]/sum2*sum(d1[N-1][:i])/sum1 for i in range(1,61))
print ans
