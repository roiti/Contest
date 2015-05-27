import math
pi = math.pi
c = int(raw_input())
r,R = map(int,raw_input().split())
r,R = (R-r)/2.0, (R+r)/2.0
print 2*(pi**2)*(r**2)*R*c