y = input()
m = input()
d = input()
if m <= 2:
    m += 12
    y -= 1
print 735369 - (365*y + int(y/4.0) - int(y/100.0) + int(y/400.0) + int((306*(m+1))/10.0) + d -429)
