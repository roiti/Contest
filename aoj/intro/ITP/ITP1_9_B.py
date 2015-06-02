while True:
    card = raw_input()
    if card == "-":
        break
    m = int(raw_input())
    for shuffle in range(m):
        h =int(raw_input())
        card = card[h:] + card[:h]
    print card

