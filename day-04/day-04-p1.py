def check_score(string):
    card = string.strip().split(":")[1].split("|")

    winning_list = [
        int(number)
        for number in string.strip().split(":")[1].split("|")[0].strip().split()
    ]

    score = 0
    for number in card[1].strip().split():
        if int(number) in winning_list:
            score += 1
    if score != 0:
        if score == 1:
            return 1
        else:
            return 2 ** (score - 1)
    return 0


def total_score(text):
    lines = text.strip().split("\n")
    total_score = 0
    for line in lines:
        total_score += check_score(line)
    return total_score


with open(".\day-04\input.txt") as f:
    input = f.read()


print(total_score(input))
