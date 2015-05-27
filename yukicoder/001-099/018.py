alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
S = raw_input()
ans = ""
for i in range(len(S)):
    ans += alpha[(26+alpha.index(S[i])-i%26-1)%26]
print ans