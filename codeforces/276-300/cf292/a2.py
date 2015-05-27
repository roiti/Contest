a,b,s = map(abs,map(int,raw_input().split()))
print "Yes" if a+b <= s and (a+b)%2 == s%2 else "No"
