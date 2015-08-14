import copy
 
def solve(xx,yy):
    def dfs(x,y,i):
        if 0 <= x < 10 and 0 <= y < 10 and B[y][x] == "o":
            B[y][x] = i
            dfs(x+1,y,i); dfs(x,y+1,i)
            dfs(x-1,y,i); dfs(x,y-1,i)
            
    B = copy.deepcopy(A)
    B[yy][xx] = "o"
    cnt = 0
    for y in range(10):
        for x in range(10):
            if B[y][x] == "o":
                dfs(x,y,cnt)
                cnt += 1
    return True if cnt == 1 else False
    
 
A = [list(raw_input()) for _ in range(10)]
flag = False
for y in range(10):
    for x in range(10):
        if A[y][x] == "x":
            if solve(x,y):
                flag = True
                break
    if flag: break
print "YES" if flag else "NO"
