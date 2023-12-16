with open(".\day-15\input.txt") as f:
    input_data = f.read()

strings = input_data.strip().split(",")

result = 0
for string in strings:
    value = 0
    for char in string:
        value = (value + ord(char)) * 17 % 256
    result += value

print(result)
