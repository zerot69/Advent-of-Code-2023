with open(".\day-08\input.txt") as f:
    lines = f.read().strip().split("\n")

instructions = [0 if char == "L" else 1 for char in lines[0]]

step = 0
node = "AAA"
node_dict = {line[0:3]: (line[7:10], line[12:15]) for line in lines[2:]}

while node != "ZZZ":
    node = node_dict[node][instructions[step % len(instructions)]]
    step += 1

print(step)
