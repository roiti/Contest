s = raw_input()
s = s.lower()
fi = fc = ft = False
for i in s:
    if i == "i":
        fi = True
    elif fi and i == "c":
        fc = True
    elif fi and fc and i == "t":
        ft = True
    break
print "YES" if fi and fc and ft else "NO"
