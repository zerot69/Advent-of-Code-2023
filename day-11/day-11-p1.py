with open(".\day-11\input.txt") as f:
    input_data = f.read()

data = input_data.strip().split("\n")
map = set(
    (i, index)
    for index, line in enumerate(data)
    for i, c in enumerate(line)
    if c == "#"
)

rows = set(y for x, y in map)
columns = set(x for x, y in map)

pairs = 0
total_distance = 0
distances = {}

for start_galaxy in map:
    for end_galaxy in map:
        if start_galaxy < end_galaxy:
            distance = abs(end_galaxy[0] - start_galaxy[0]) + abs(
                end_galaxy[1] - start_galaxy[1]
            )
            for i in range(
                min(start_galaxy[1], end_galaxy[1]),
                max(start_galaxy[1], end_galaxy[1]) + 1,
            ):
                if i not in rows:
                    distance += 1
            for i in range(
                min(start_galaxy[0], end_galaxy[0]),
                max(start_galaxy[0], end_galaxy[0]) + 1,
            ):
                if i not in columns:
                    distance += 1
            distances[(start_galaxy, end_galaxy)] = distance
            distances[(end_galaxy, start_galaxy)] = distance
            pairs += 1
            total_distance += distance

print(pairs)
print(total_distance)
