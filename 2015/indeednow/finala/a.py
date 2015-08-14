n = int(raw_input())
a = sorted(map(int,raw_input().split()))
mn = 10**10
mx = 0
for i in xrange(n/2):
    team = a.pop(0)+a.pop()
    mn = min(mn,team)
    mx = max(mx,team)
print mx-mn
