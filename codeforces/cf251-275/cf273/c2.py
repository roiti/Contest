r,g,b = sorted(map(int,raw_input().split()))

print r+g if (r+g)*2 < b else (r+g+b)/3
