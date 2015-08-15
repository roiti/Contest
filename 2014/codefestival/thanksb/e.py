import sys
sys.setrecursionlimit(10000)
 
def solve(r,c):
    if 0 <= r < R and 0 <= c < C and A[r][c] == "#":
        A[r][c] = "0"
        solve(r+1,c);solve(r-1,c);solve(r,c+1);solve(r,c-1)
            
R,C = map(int,raw_input().split())
rs,cs = map(int,raw_input().split())
rg,cg = map(int,raw_input().split())
A = [["."]*C for _ in range(R)]
N = int(raw_input())
for loop in range(N):
    r,c,h,w = map(int,raw_input().split())
    for i in range(h):
        A[r+i-1][c-1:c+w-1] = "#"*w
solve(rs-1,cs-1)
print "YES" if A[rs-1][cs-1] == A[rg-1][cg-1] == "0" else "NO"
