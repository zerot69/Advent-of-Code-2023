def spin_cycle():
    for col in range(x):
        lim = 0
        for row in range(y):
            if grid[row][col] == "#":
                lim = row + 1
            elif grid[row][col] == "O":
                if row > lim:
                    grid[lim][col], grid[row][col] = grid[row][col], grid[lim][col]
                lim += 1
    for row in range(y):
        lim = 0
        for col in range(x):
            if grid[row][col] == "#":
                lim = col + 1
            elif grid[row][col] == "O":
                if col > lim:
                    grid[row][lim], grid[row][col] = grid[row][col], grid[row][lim]
                lim += 1
    for col in range(x):
        lim = y - 1
        for row in reversed(range(y)):
            if grid[row][col] == "#":
                lim = row - 1
            elif grid[row][col] == "O":
                if row < lim:
                    grid[lim][col], grid[row][col] = grid[row][col], grid[lim][col]
                lim -= 1
    for row in range(y):
        lim = x - 1
        for col in reversed(range(x)):
            if grid[row][col] == "#":
                lim = col - 1
            elif grid[row][col] == "O":
                if col < lim:
                    grid[row][lim], grid[row][col] = grid[row][col], grid[row][lim]
                lim -= 1


with open(".\day-14\input.txt") as f:
    input_data = f.read()

grid = [list(row) for row in input_data.split("\n")]
y, x = len(grid), len(grid[0])
loads = []
history = {}
for i in range(300):
    spin_cycle()
    total_load = sum((grid[r][c] == "O") * (y - r)
                     for r in range(y) for c in range(x))
    loads.append(total_load)

    if i > 20:
        state_hash = str(loads[-20:])
        if state_hash in history:
            cycle_start = history[state_hash]
            cycle_length = i - cycle_start
            break
        history[state_hash] = i

target = 1000000000
offset = (target - cycle_start) % cycle_length - 1
print(loads[cycle_start + offset])
