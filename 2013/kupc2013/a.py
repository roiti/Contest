n,q = map(int,raw_input().split())
old = "kogakubu10gokan"
for i in range(n):
    year,new = map(str,raw_input().split())
    if int(year) >= q:
        print new if int(year) == q else old
        break
    old = new
else:
    print old
