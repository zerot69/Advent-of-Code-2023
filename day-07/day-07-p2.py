with open(".\day-07\input.txt") as f:
    lines = f.read().strip().split("\n")

strengths = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0,
}
hands = []
for i_index, line in enumerate(lines):
    hands.append(line.strip().split(" "))


def get_type(hand):
    cards = {}
    jokers = 0
    for char in hand:
        if char == "J":
            jokers += 1
        else:
            if char in cards:
                cards[char] += 1
            else:
                cards[char] = 1
    cards = {
        k: v for k, v in sorted(cards.items(), key=lambda item: item[1], reverse=True)
    }
    values = list(cards.values())
    if jokers == 5 or (values[0] + jokers == 5):
        print("Five of a kind")
        return 6
    elif values[0] + jokers == 4:
        print("Four of a kind")
        return 5
    elif values[0] + jokers == 3:
        if values[1] == 2:
            print("Full house")
            return 4
        else:
            print("Three of a kind")
            return 3
    elif values[0] == 2 and values[1] == 2:
            print("Two pair")
            return 2
    elif values[0] == 2 or jokers:
        print("One pair")
        return 1
    else:
        print("High card")
        return 0


def get_card_strength(hand):
    return [strengths[card] for card in hand]


ranks = []
ranked_hands = [(get_type(hand[0]), hand) for hand in hands]
ranked_hands.sort(key=lambda x: (x[0], get_card_strength(x[1][0])))
ranks = [hand for _, hand in ranked_hands]
result = 0

for index, hand in enumerate(ranks):
    print(hand)
    result += int(hand[1]) * (index + 1)

print(result)
