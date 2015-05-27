import math
x,y = map(int,raw_input().split())
print int(2*math.ceil(2*(x*x+y*y)**0.5+1e-9)/2)