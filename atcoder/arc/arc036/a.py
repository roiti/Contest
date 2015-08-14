N, K = map(int, raw_input().split())
t = [int(raw_input()) for i in xrange(N)]
 
k = t[0]+t[1]
for day in xrange(2,N):
    k += t[day]
    if k < K:
        print day+1
        break
    k -= t[day-2]
else:
    print -1
