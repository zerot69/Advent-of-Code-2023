import math


with open(".\day-08\input.txt") as f:
    lines = f.read().strip().split("\n")

instructions = [0 if char == "L" else 1 for char in lines[0]]

results = []
nodes = []
for index, line in enumerate(lines):
    if index > 1:
        if line[2] == "A":
            nodes.append(line[0:3])
node_dict = {line[0:3]: (line[7:10], line[12:15]) for line in lines[2:]}

for node in nodes:
    step = 0
    while node[2] != "Z":
        node = node_dict[node][instructions[step % len(instructions)]]
        step += 1
    results.append(step)

print(results)
print(math.lcm(*results))

# Code ran forever, gave up, checked subreddit for hints, found LCM solution, implemented it, got correct answer, still no idea why it works
