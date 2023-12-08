digits = {
    "oneight": 18,
    "twone": 21,
    "threight": 38,
    "fiveine": 58,
    "eightwo": 82,
    "eighthree": 83,
    "nineight": 98,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def extract_digits(word):
    for digit in digits:
        word = word.replace(digit, str(digits[digit]))

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
        print(extract_digits(line))
        total_sum += extract_digits(line)

    return total_sum


with open(".\day-01\input.txt") as f:
    input = f.read()

print(sum_of_calibration_values(input))
