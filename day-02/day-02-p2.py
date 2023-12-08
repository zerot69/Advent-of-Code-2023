def check_color_max(string):
    color_max = {"red": 0, "green": 0, "blue": 0}
    game = string.split(":")[1].split(";")
    for turn in game:
        for color in turn.split(","):
            if (
                int(color.strip().rsplit(" ", 1)[0])
                > color_max[color.strip().rsplit(" ", 1)[1]]
            ):
                color_max[color.strip().rsplit(" ", 1)[1]] = int(
                    color.strip().rsplit(" ", 1)[0]
                )
    power = 1
    for color in color_max:
        power *= color_max[color]
    return power


def sum_of_game_power(text):
    lines = text.strip().split("\n")
    total_sum = 0
    for line in lines:
        total_sum += check_color_max(line)
    return total_sum


with open(".\day-02\input.txt") as f:
    input = f.read()

print(sum_of_game_power(input))
