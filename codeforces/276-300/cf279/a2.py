n = int(raw_input())
child = map(int,raw_input().split())
prog,math,sport = [],[],[]
for i in range(n):
    if   child[i] == 1: prog.append(i+1)
    elif child[i] == 2: math.append(i+1)
    else              : sport.append(i+1)
ans = []
while math and prog and sport:
    ans.append([prog.pop(),math.pop(),sport.pop()])
print len(ans)
for line in ans:
    print " ".join(map(str,line))
