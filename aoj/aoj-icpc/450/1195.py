ans = []
def search(s,c):
    if c == "a":
        ans.append(s)
        return

    for i in xrange(len(s)):
        if s[i] == c: return
    
        if s[i] == chr(ord(c)-1):
            t = list(s[:])
            t[i] = c
            t = "".join(t)
            
            search(t, chr(ord(c)-1))
    search(s, chr(ord(c)-1))
            
while 1:
    S = raw_input()
    if S == "#": break

    ans = []
    search(S,"z")
    
    ans = sorted(list(set(ans)))
    print len(ans)
    if len(ans) <= 10:
        for a in ans:
            print a
    else:
        for i in xrange(5):
            print ans[i]
        for i in xrange(5):
            print ans[len(ans)-5+i]

