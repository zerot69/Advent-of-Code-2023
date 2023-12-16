def mirror(grid, vertical=True):
    total_row = len(grid.split("\n"))
    total_col = len(grid.split("\n")[0])
    list_len = total_col if vertical else total_row
    list_ = ["" for _ in range(list_len)]
    for i in range(list_len):
        for j in range(total_row if vertical else total_col):
            list_[
                i] += grid.split("\n")[j][i] if vertical else grid.split("\n")[i][j]
    for index in range(1, len(list_)):
        length = min(index, list_len - index)
        side_1 = side_2 = ""
        for i in range(index - length, index):
            side_1 += list_[i]
        for i in range(index + length - 1, index - 1, -1):
            side_2 += list_[i]
        if side_1 == side_2:
            return index
    return None


with open(".\day-13\input.txt") as f:
    input_data = f.read()

data = input_data.strip().split("\n\n")
result = 0
for part in data:
    result += mirror(part, vertical=True) or mirror(part, vertical=False) * 100

print(result)
