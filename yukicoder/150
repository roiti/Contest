T = int(raw_input())
for loop in xrange(T):
    S = raw_input()
    ans = 12
    for i in range(len(S)-10):
        for j in range(i+4,len(S)-6):
            cnt = 0
            for k in range(4):
                if S[i+k] != "good"[k]: cnt += 1
            for k in range(7):
                if S[j+k] != "problem"[k]: cnt += 1
            ans = min(ans, cnt)
    print ans
    
