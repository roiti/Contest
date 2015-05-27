N = int(raw_input())
item = [0]*10
for loop in xrange(N):
    for i in map(int,raw_input().split()):
        item[i-1] += 1
ans = 0
for i in xrange(10):
    ans += item[i]/2
    item[i] %= 2
ans += item.count(1)/4
print ans