import re
import itertools


def go_forwards(line, start=0):
    return "".join(itertools.takewhile(str.isdigit, line[start:]))


def go_backwards(line, end=0):
    return "".join(itertools.takewhile(str.isdigit, reversed(line[:end])))[::-1]


with open(".\day-03\input.txt") as f:
    input = f.read()

lines = input.strip().split("\n")
result = 0

for index, line in enumerate(lines):
    line = "".join(line.strip())
    if index == 0:
        line_prev = line
    if index >= len(lines) - 1:
        line_next = line
    else:
        line_next = lines[index + 1]

    for pos, char in enumerate(line):
        if char == "*":
            adjacent = 0
            if line[pos - 1].isdigit():
                adjacent += 1
            if line[pos + 1].isdigit():
                adjacent += 1
            adjacent += len(re.findall(r"\d+", line_prev[pos - 1 : pos + 2]))
            adjacent += len(re.findall(r"\d+", line_next[pos - 1 : pos + 2]))
            if adjacent != 2:
                continue

            map = list()
            if line[pos - 1].isdigit():
                map.append(go_backwards(line, end=pos))
            if line[pos + 1].isdigit():
                map.append(go_forwards(line, start=pos + 1))
            if line_prev[pos].isdigit():
                map.append(
                    go_backwards(line_prev, end=pos + 1)
                    + go_forwards(line_prev, start=pos + 1)
                )
            else:
                if line_prev[pos - 1].isdigit():
                    map.append(go_backwards(line_prev, end=pos))
                if line_prev[pos + 1].isdigit():
                    map.append(go_forwards(line_prev, start=pos + 1))
            if line_next[pos].isdigit():
                map.append(
                    go_backwards(line_next, end=pos + 1)
                    + go_forwards(line_next, start=pos + 1)
                )
            else:
                if line_next[pos - 1].isdigit():
                    map.append(go_backwards(line_next, end=pos))
                if line_next[pos + 1].isdigit():
                    map.append(go_forwards(line_next, start=pos + 1))
            result += int(map[0]) * int(map[1])

    line_prev = line

print(result)
