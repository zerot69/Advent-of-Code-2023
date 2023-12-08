instances = [1 for i in range(193)]


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
    for i in range(score):
        instances[int(string.strip().split(":")[0].split()[1]) + i] += instances[
            int(string.strip().split(":")[0].split()[1]) - 1
        ]
    return 0


def total_score(text):
    lines = text.strip().split("\n")
    for line in lines:
        check_score(line)
    return sum(instances)


with open(".\day-04\input.txt") as f:
    input = f.read()


print(total_score(input))
