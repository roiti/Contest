S = raw_input().split()
while 1:
    change = False
    for i in xrange(len(S)-2):
        if S[i] == S[i+1] == "not" and S[i+2] != "not":
            S = S[:i]+S[i+2:]
            change = True
            break
    if not change: break
print " ".join(S)
