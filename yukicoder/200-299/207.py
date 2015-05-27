import strutils

var AB = readLine(stdin).split().map(parseInt)

for i in AB[0]..AB[1]:
    if i mod 3 == 0 or "3" in $i:
        echo($i)
