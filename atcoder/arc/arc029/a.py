N = int(raw_input())
t = [int(raw_input()) for i in range(N)]
ans = 10**10
if N <= 2:
    ans = max(t)
elif N == 3:
    for i in [0,1]:
        for j in [0,1]:
            plate = [t[0],0]
            plate[i] += t[1]
            plate[j] += t[2]
            ans = min(ans,max(plate))
else:
    for i in [0,1]:
        for j in [0,1]:
            for k in [0,1]:
                plate = [t[0],0]
                plate[i] += t[1]
                plate[j] += t[2]
                plate[k] += t[3]
                ans = min(ans,max(plate))
print ans
