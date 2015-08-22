s = raw_input()
if s == "{}":
    print "dict"
    exit()
depth = 0
for si in s:
    if si == "{":
        depth += 1
    if si == "}":
        depth -= 1
    if si == "," and depth == 1:
        print "set"
        break
    if si == ":" and depth == 1:
        print "dict"
        break
else:
    print "set"
