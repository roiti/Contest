N = int(raw_input())-2014
M = N%400
ans = N/400*57
k = 0
for i in xrange(2015,2015+M):
    if i%400 == 0 or not (i%100 == 0) and i%4 == 0: k += 2
    else: k += 1
    k %= 7
    if k == 0: ans += 1
print ans