with open(".\day-14\input.txt") as f:
    input_data = f.read()

data = input_data.strip().split("\n")
load = 0
data_length = len(data)
for col_index in range(len(data[0])):
    rocks = 0
    limit = data_length
    for row_index in range(data_length):
        if data[row_index][col_index] == "O":
            rocks += 1
        elif data[row_index][col_index] == "#":
            load += sum(range(limit, limit - rocks, -1))
            limit = data_length - row_index - 1
            rocks = 0
        if row_index == data_length - 1:
            load += sum(range(limit, limit - rocks, -1))

print(load)
