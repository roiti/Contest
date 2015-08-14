ref = "zrbcdwtjfqlvsxpmhkng"
N = int(raw_input())
W = raw_input().lower().split()
ans = ""
for w in W:
    flag = 0
    for a in w:
        try:
            yans += str(ref.index(a) / 2)
            flag = 1
        except:
            pass
    ans += " " * flag
print ans[:-1]
