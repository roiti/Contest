def to_sec(a):
    h,m,s = map(int,a.split(":"))
    return 3600*h+60*m+s

while 1:
    n = int(raw_input())
    if n == 0: break
    used = [0]*86401
    for loop in range(n):
        a,b = raw_input().split()
        a,b = to_sec(a),to_sec(b)
        used[a] += 1
        used[b] -= 1
    for i in range(1,86401):
        used[i] += used[i-1]
    print max(used)

