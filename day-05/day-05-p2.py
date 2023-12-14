import re

with open(".\day-05\input.txt") as f:
    segments = f.read().split("\n\n")
intervals = []

for seed in re.findall(r"(\d+) (\d+)", segments[0]):
    x_1, dx = map(int, seed)
    x_2 = x_1 + dx
    intervals.append((x_1, x_2, 1))

min = float("inf")
while intervals:
    x_1, x_2, level = intervals.pop()
    if level == 8:
        min = min(x_1, min)
        continue

    for conversion in re.findall(r"(\d+) (\d+) (\d+)", segments[level]):
        z, y_1, dy = map(int, conversion)
        y_2 = y_1 + dy
        diff = z - y_1
        if x_2 <= y_1 or y_2 <= x_1:
            continue
        if x_1 < y_1:
            intervals.append((x_1, y_1, level))
            x_1 = y_1
        if y_2 < x_2:
            intervals.append((y_2, x_2, level))
            x_2 = y_2
        intervals.append((x_1 + diff, x_2 + diff, level + 1))

    else:
        intervals.append((x_1, x_2, level + 1))

print(min)
