def find_directions(x, y, last_x, last_y):
    directions = []
    direction_map = [
        (0, -1, "|", 0, -1),  # moving up straight
        (0, -1, "7", -1, -1),  # moving up left
        (0, -1, "F", 1, -1),  # moving up right
        (0, 1, "|", 0, 1),  # moving down straight
        (0, 1, "J", -1, 1),  # moving down left
        (0, 1, "L", 1, 1),  # moving down right
        (-1, 0, "-", -1, 0),  # moving left straight
        (-1, 0, "L", -1, -1),  # moving left up
        (-1, 0, "F", -1, 1),  # moving left down
        (1, 0, "-", 1, 0),  # moving right straight
        (1, 0, "J", 1, -1),  # moving right up
        (1, 0, "7", 1, 1),  # moving right down
    ]
    if data[y][x] == "S":
        for check_x, check_y, symbol, dx, dy in direction_map:
            try:
                if data[y + check_y][x + check_x] == symbol:
                    directions.append([x + dx, y + dy, x, y])
            except:
                pass
    else:
        for check_x, check_y, symbol, dx, dy in direction_map:
            if data[y][x] == symbol:
                directions.append([x - check_x, y - check_y, x, y])
    if len(directions) == 0:
        print("can't move", data[y], x)
    try:
        directions.remove([last_x, last_y, x, y])
    except:
        pass
    return directions


with open(".\day-10\input.txt") as f:
    input = f.read()

data = input.strip().split("\n")

step = 0
for index, line in enumerate(data):
    if line.find("S") != -1:
        x = last_x = line.find("S")
        y = last_y = index
        if step == 0:
            last_x = -1
            last_y = -1
            while data[y][x] != "S" or step == 0:
                x, y, last_x, last_y = find_directions(x, y, last_x, last_y)[0]
                step += 1

print(round(step / 2))
