a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
rank = sorted([a,b,c])[::-1]
print rank.index(a)+1
print rank.index(b)+1
print rank.index(c)+1
