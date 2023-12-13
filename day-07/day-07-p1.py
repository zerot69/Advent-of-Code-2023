with open(".\day-07\input.txt") as f:
    lines = f.read().strip().split("\n")

strengths = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
}
hands = []
for i_index, line in enumerate(lines):
    hands.append(line.strip().split(" "))


def get_type(hand):
    cards = {}
    for char in hand:
        if char in cards:
            cards[char] += 1
        else:
            cards[char] = 1
    cards = {
        k: v for k, v in sorted(cards.items(), key=lambda item: item[1], reverse=True)
    }
    values = list(cards.values())
    if values[0] == 5:
        return 6
    elif values[0] == 4:
        return 5
    elif values[0] == 3:
        if values[1] == 2:
            return 4
        else:
            return 3
    elif values[0] == 2:
        if values[1] == 2:
            return 2
        else:
            return 1
    else:
        return 0


def get_card_strength(hand):
    return [strengths[card] for card in hand]


ranks = []
ranked_hands = [(get_type(hand[0]), hand) for hand in hands]
ranked_hands.sort(key=lambda x: (x[0], get_card_strength(x[1][0])))
ranks = [hand for _, hand in ranked_hands]
result = 0

for index, hand in enumerate(ranks):
    result += int(hand[1]) * (index + 1)

print(result)
