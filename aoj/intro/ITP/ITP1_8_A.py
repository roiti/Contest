z = ""
for x in raw_input():
    if x.islower():
        z += x.upper()
    else:
        z += x.lower()

print z

