x0,y0,x1,y1,x2,y2 = map(int,raw_input().split())
print abs((x1-x0)*(y2-y0)-(x2-x0)*(y1-y0))/2.0
