num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
suit = ["D", "C", "H", "S"]
N = int(raw_input())
mn = raw_input().split()
ans = []
for s in suit:
    for n in num:
        card = s + n
        for c in mn:
            if card == c:
                ans.append(card)
print " ".join(ans)
