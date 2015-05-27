n,m,dx,dy = map(int,raw_input().split())
getsx = [0]*n
for i in range(n):
    getsx[dx*i%n] = i
starty = [0]*n
for roop in range(m):
    x,y = map(int,raw_input().split())
    starty[(y-dy*getsx[x]%n+n)%n] += 1
print 0,starty.index(max(starty))
