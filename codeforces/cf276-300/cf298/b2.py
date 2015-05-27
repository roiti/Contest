v1, v2 = map(int, raw_input().split())
t, d = map(int, raw_input().split())
speed = [0]*t
speed[0] = v1
for i in xrange(1,t-1):
    speed[i] = speed[i-1] + d
speed[-1] = v2

for i in xrange(t-2, 0, -1):
    speed[i] = min(speed[i+1]+d, speed[i])

print sum(speed)
