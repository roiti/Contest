n = int(raw_input())
refs = []
for loop in range(n):
    old,new = raw_input().split()
    for i in range(len(refs)):
        if old in refs[i]:
            refs[i].append(new)
            break
    else:
        refs.append([old,new])

print len(refs)        
for ref in refs:
    print ref[0],ref[-1]
