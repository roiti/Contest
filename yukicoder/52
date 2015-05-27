def rec(S,T):
    if S == "":
        ans.append("".join(T))
        return
    rec(S[1:] ,T+S[ 0])
    rec(S[:-1],T+S[-1])

S = raw_input()
ans = []
rec(S,"")
print len(set(ans))