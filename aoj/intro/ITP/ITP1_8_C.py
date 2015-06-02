import sys
az =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
sum_az = [0 for x in range(26)]

for x in sys.stdin.read().lower():
    for i in range(26):
        if x == az[i]:
            sum_az[i] += 1


for i in range(26):
    print ("%s : %d" % (az[i], sum_az[i]))
                

