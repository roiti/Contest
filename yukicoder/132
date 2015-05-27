import math
def cross(A,B):
    a = A[1]*B[2]-A[2]*B[1]
    b = A[2]*B[0]-A[0]*B[2]
    c = A[0]*B[1]-A[1]*B[0]
    return a,b,c
    
def dist(i,j,k):
    AB = [XYZ[j][l]-XYZ[i][l] for l in range(3)]
    AC = [XYZ[k][l]-XYZ[i][l] for l in range(3)]
    a,b,c = cross(AB,AC)
    d = -(a*XYZ[i][0]+b*XYZ[i][1]+c*XYZ[i][2])
    return abs(a*P[0]+b*P[1]+c*P[2]+d)/math.sqrt(a**2+b**2+c**2)
    
N = int(raw_input())
P = map(float,raw_input().split())
XYZ = [map(float,raw_input().split()) for _ in range(N)]

ans = 0.0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            ans += dist(i,j,k)
print "%.10f"%ans
        