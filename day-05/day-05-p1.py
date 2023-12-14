import re

with open(".\day-05\input.txt") as f:
    segments = f.read().split("\n\n")

seeds = [int(seed) for seed in re.findall(r"\d+", segments[0])]
min = float("inf")
for x in seeds:
    for segment in segments[1:]:
        for conversion in re.finditer(r"(\d+) (\d+) (\d+)", segment):
            destination, start, delta = map(int, conversion.groups())
            if start <= x < start + delta:
                x += destination - start
                break
    min = min(x, min)

print(min)
