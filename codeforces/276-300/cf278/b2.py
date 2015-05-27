def judge(A):
    return True if sum(A)/4.0 == (A[1]+A[2])/2.0 == A[3]-A[0] else False
    
n = int(raw_input())
A = sorted([int(raw_input()) for _ in range(n)])
if   n == 4:
    print "YES" if sum(A)/4.0 == (A[1]+A[2])/2.0 == (A[3]*1.0-A[0]) else "NO"
elif n == 3:
    a,b,c = A[:]
    ans = 0
    if   judge([a,b,c,3*a]): ans = 3*a
    elif judge([a,b,4*a-b,c]): ans = 4*a-b
    elif (a+b)%4 == 0 and judge([(a+b)/4,a,b,c]): ans = (a+b)/4
    print "YES\n%s"%ans if ans > 0 else "NO"
elif n == 2:
    a,b = A[:]
    ans1 = ans2 = 0
    if   judge([a,b,4*a-b,3*a]): ans1,ans2 = 4*a-b,3*a
    elif b == 3*a: ans1,ans2 = a,b
    elif (b+c)%4 == 0 and judge([(b+c)/4,a,b,3*(b+c)/4]): ans1,ans2 = (b+c)/4,3*(b+c)/4
    elif b%3 == 0 and judge([b/3,a,4*b/3-a,b]): ans1,ans2 = b/3,4*b/3-a
    print "YES\n%s\n%s"%(ans1,ans2) if ans1*ans2 > 0 else "NO"
elif n == 1:
    print "YES\n%s\n%s\n%s"%(A[0],3*A[0],3*A[0])
else:
    print "YES\n%s\n%s\n%s\n%s"%(1,1,3,3)
