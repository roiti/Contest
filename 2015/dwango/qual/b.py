S = raw_input().replace("25","X")
ans = 0
i = j = 0
seq = 0
while j < len(S):
    if S[i] == "X":
        if S[j] == "X":
            seq += 1
            j += 1
        else:
            ans += seq*(seq+1)/2
            i = j
            seq = 0
    else:
        i += 1
        j = i
print ans+seq*(seq+1)/2
