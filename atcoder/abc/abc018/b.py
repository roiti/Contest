S = raw_input()
N = int(raw_input())
for loop in range(N):
    l,r = map(int,raw_input().split())
    l -= 1; r -= 1
    S = S[:l] + S[l:r+1][::-1] + S[r+1:]
print S
