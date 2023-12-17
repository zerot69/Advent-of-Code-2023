def mirror(grid, vertical=True, old_mirror=None):
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
        if old_mirror == None:
            if side_1 == side_2:
                return index
        elif old_mirror != None:
            if side_1 == side_2 and index != old_mirror:
                return index
    return None


with open(".\day-13\input.txt") as f:
    input_data = f.read()

data = input_data.strip().split("\n\n")
result = 0
for part in data:
    lines = part.split("\n")
    smudge_found = False
    old_mirror_vertical = mirror(part, vertical=True)
    old_mirror_horizontal = mirror(part, vertical=False)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            new_lines = lines.copy()
            if char == ".":
                new_lines[i] = new_lines[i][:j] + "#" + new_lines[i][j + 1:]
            elif char == "#":
                new_lines[i] = new_lines[i][:j] + "." + new_lines[i][j + 1:]
            new_lines = "\n".join(new_lines)
            mirror_vertical = mirror(
                new_lines, vertical=True, old_mirror=old_mirror_vertical)
            if mirror_vertical and mirror_vertical != old_mirror_vertical:
                result += mirror_vertical
                smudge_found = True
                break
            else:
                mirror_horizontal = mirror(
                    new_lines, vertical=False, old_mirror=old_mirror_horizontal)
                if mirror_horizontal and mirror_horizontal != old_mirror_horizontal:
                    result += mirror_horizontal * 100
                    smudge_found = True
                    break
        if smudge_found:
            break

print(result)
