names = ["TAKAHASHIKUN", "Takahashikun", "takahashikun"]
N = int(raw_input())
words = raw_input()[:-1].split()
ans = sum(sum([word == name for word in words]) for name in names)
print ans
