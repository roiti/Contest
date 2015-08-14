def solve(s):
    if s == "": return True
    if s[-1] in "oku": return solve(s[:-1])
    if len(s) > 1 and s[-2:] == "ch": return solve(s[:-2])
    return False
 
print "YES" if solve(raw_input()) else "NO"
