N,K = map(int,raw_input().split())
a = [int(raw_input()) for i in range(N)]
S = 0
for day in range(N):
    S += a[day]
    if S >= K:
        print day+1
        break
