import re


def check_part_engine(input_string):
    return any(
        char.isalpha() or (not char.isdigit() and char != ".") for char in input_string
    )


with open(".\day-03\input.txt") as f:
    input = f.read()

lines = input.strip().split("\n")
sum = 0
line_num = 0
for line in lines:
    line_num += 1
    numbers = re.findall(r"\d+", line)
    numbers = [int(num) for num in numbers]
    for number in numbers:
        start_pos = max(0, line.find(str(number)) - 1)
        char_len = len(str(number))
        end_pos = line.find(str(number)) + char_len + 1
        adjacent = False
        if line_num > 1:
            if check_part_engine(lines[line_num - 2][start_pos:end_pos]):
                adjacent = True
        if check_part_engine(lines[line_num - 1][start_pos:end_pos]):
            adjacent = True
        if line_num < len(lines):
            if check_part_engine(lines[line_num][start_pos:end_pos]):
                adjacent = True
        line = line.replace(str(number), len(str(number)) * ".", 1)
        if adjacent:
            sum += int(number)


print(sum)
