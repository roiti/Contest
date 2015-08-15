A = [[0] * 1001 for i in xrange(1001)]
x, y = 500, 500
dx, dy = 0, 1
step = []
for i in xrange(35000):
    if A[y][x] == 0:
        dx, dy = dy, -dx
        A[y][x] = 1
    else:
        dx, dy = -dy, dx
        A[y][x] = 0
    x, y = x + dx, y + dy
    step.append(A[y][x])
 
N = int(raw_input())
if N <= 35000:
    print step[N - 1]
else:
    step = step[-5200:]
    print step[(N - 35001) % 5200]
