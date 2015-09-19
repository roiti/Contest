D, S = map(int, raw_input().split())
D *= 10
S = int(10 * S / 60.0 + 0.5)

if S < 3: a = "C"
elif D < 1125 or D >= 34875: a = "N"
elif D < 3375: a = "NNE"
elif D < 5625: a = "NE"
elif D < 7875: a = "ENE"
elif D < 10125: a = "E"
elif D < 12375: a = "ESE"
elif D < 14625: a = "SE"
elif D < 16875: a = "SSE"
elif D < 19125: a = "S"
elif D < 21375: a = "SSW"
elif D < 23625: a = "SW"
elif D < 25875: a = "WSW"
elif D < 28125: a = "W"
elif D < 30375: a = "WNW"
elif D < 32625: a = "NW"
else: a = "NNW"

if S <= 2: b = 0
elif S <= 15: b = 1
elif S <= 33: b = 2
elif S <= 54: b = 3
elif S <= 79: b = 4
elif S <= 107: b = 5
elif S <= 138: b = 6
elif S <= 171: b = 7
elif S <= 207: b = 8
elif S <= 244: b = 9
elif S <= 284: b = 10
elif S <= 326: b = 11
else: b = 12

print a, b
