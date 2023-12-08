color_max = {"red": 12, "green": 13, "blue": 14}


def check_game_possible(string):
    game = string.split(":")[1].split(";")
    for turn in game:
        for color in turn.split(","):
            if (
                int(color.strip().rsplit(" ", 1)[0])
                > color_max[color.strip().rsplit(" ", 1)[1]]
            ):
                return 0
    return int(string.split(":")[0].strip().rsplit(" ", 1)[1])


def sum_of_game_ids(text):
    lines = text.strip().split("\n")
    total_sum = 0
    for line in lines:
        total_sum += check_game_possible(line)
    return total_sum


with open(".\day-02\input.txt") as f:
    input = f.read()

print(sum_of_game_ids(input))
