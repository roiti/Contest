sign_ref = { "1": 1,  "i": 1,  "j": 1,  "k": 1,
            "11": 1, "1i": 1, "1j": 1, "1k": 1,
            "i1": 1, "ii":-1, "ij": 1, "ik":-1,
            "j1": 1, "ji":-1, "jj":-1, "jk": 1,
            "k1": 1, "ki": 1, "kj":-1, "kk":-1}

mul = { "1":"1",  "i":"i",  "j":"j",  "k":"k",
       "11":"1", "1i":"i", "1j":"j", "1k":"k",
       "i1":"i", "ii":"1", "ij":"k", "ik":"j",
       "j1":"j", "ji":"k", "jj":"1", "jk":"i",
       "k1":"k", "ki":"j", "kj":"i", "kk":"1"}

T = int(raw_input())
for loop in xrange(T):
    L, X = map(int, raw_input().split())
    if X > 8: X = 8+X%4
    S = raw_input()*X

    sign = 1
    e = ""
    char = "i"
    for i in xrange(L*X):
        sign *= sign_ref[e+S[i]]
        e = mul[e+S[i]]
        if char != "k" and e == char and sign == 1:
            char = {"i":"j", "j":"k"}[char]
            e = ""
            
    judge = (e == char == "k" and sign == 1)
    print "Case #%d: %s"%(loop+1, "YES" if judge else "NO")

