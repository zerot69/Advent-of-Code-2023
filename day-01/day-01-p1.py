def extract_digits(word):
    first_number = None
    last_number = None

    for char in word:
        if char.isdigit():
            if first_number is None:
                first_number = int(char)
            last_number = int(char)

    return first_number * 10 + last_number if first_number is not None else 0


def sum_of_calibration_values(text):
    lines = text.strip().split("\n")
    total_sum = 0

    for line in lines:
        print(line, extract_digits(line))
        total_sum += extract_digits(line)

    return total_sum


with open(".\day-01\input.txt") as f:
    input = f.read()

print(sum_of_calibration_values(input))
