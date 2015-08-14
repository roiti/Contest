N = int(raw_input())

holidays = set(raw_input() for i in xrange(N))
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = 6
ans = seq = alt = 0
holiday = False

for month in xrange(1, 13):
    for d in xrange(1, days[month - 1] + 1):
        if str(month) + "/" + str(d) in holidays:
            if week <= 4: holiday = True
            else: alt += 1
        if not (week >= 5 or holiday or alt > 0):
            ans = max(ans, seq)
            seq = 0
        elif week >= 5:
            seq += 1
        elif holiday:
            seq += 1
            holiday = False
        elif alt > 0:
            seq += 1
            alt -= 1
        week = (week + 1) % 7
    
print max(ans, seq)
