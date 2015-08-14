Y = int(raw_input())
print ["NO", "YES"][(Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0]

