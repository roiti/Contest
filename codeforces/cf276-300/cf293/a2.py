s = raw_input()
t = raw_input()
n = len(s)
for i in xrange(n):
    d = ord(t[i])-ord(s[i])
    if d > 1:
        print s[:i]+chr(ord(s[i])+1)+s[i+1:]        
        exit()
    if d == 1 and i < n-1:
        for j in xrange(i+1,n):
            if s[j] < "z":
                print s[:i+1]+"z"*(n-i-1)
                exit()
            if t[j] > "a":
                print t[:i+1]+"a"*(n-i-1)
                exit()
print "No such string"
