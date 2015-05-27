def isX(a,b,c):
    det = a*bb-aa*b
    if det == 0: return False
    x = (b*cc-bb*c)*1.0/det
    y = -(a*cc-aa*c)*1.0/det
    if min(x1,x2) <= x <= max(x1,x2) and min(y1,y2) <= y <= max(y1,y2):
        return True
    else:
        False
        
x1,y1 = map(int,raw_input().split())
x2,y2 = map(int,raw_input().split())
aa,bb,cc = y2-y1,-(x2-x1),(x2-x1)*y2-(y2-y1)*x2
n = int(raw_input())
ans = 0
for loop in range(n):
    a,b,c = map(int,raw_input().split())
    if isX(a,b,c):
        ans += 1
print ans
