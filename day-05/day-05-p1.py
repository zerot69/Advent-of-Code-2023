import re

with open(".\day-05\input.txt") as f:
    input = f.read()
segments = input.split("\n\n")
seeds = re.findall(r"\d+", segments[0])
print("seeds", seeds)

min_location = float("inf")
for x in map(int, seeds):
    for segment in segments[1:]:
        for conversion in re.findall(r"(\d+) (\d+) (\d+)", segment):
            destination, start, delta = map(int, conversion)
            if x in range(start, start + delta):
                x += destination - start
                break

    min_location = min(x, min_location)

print(min_location)
