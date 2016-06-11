ans = ["Do", "Re", "Mi", "Fa", "So", "La", "Si"]
x = "WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW" 
S = raw_input()
w = 0
for i in xrange(len(x) - len(S)):
    if x[i:i + len(S)] == S:
        print ans[w%len(ans)]
        break
    if x[i] == "W": 
        w += 1
