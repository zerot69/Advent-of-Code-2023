from collections import deque

with open(".\day-10\input.txt") as f:
    data = [list(line.strip()) for line in f]

row, col = len(data), len(data[0])
graph = {}
pipes = set()
visited = set()
tile_q = set()
corner_q = deque([(0, 0)])

for x in range(row):
    for y in range(col):
        tile = data[x][y]
        adjacent = []
        if tile in '-J7S':
            adjacent.append((x, y-1))
        if tile in '-FLS':
            adjacent.append((x, y+1))
        if tile in '|F7S':
            adjacent.append((x+1, y))
        if tile in '|LJS':
            adjacent.append((x-1, y))
        if tile == 'S':
            tile_q.add((x, y))
        graph[(x, y)] = adjacent

while tile_q:
    next = set()
    for x1, y1 in tile_q:
        for x2, y2 in graph[(x1, y1)]:
            if (x1, y1) not in graph.get((x2, y2), []):
                continue
            pipe = (*sorted((x1, x2)), *sorted((y1, y2)))
            if pipe not in pipes:
                pipes.add(pipe)
                next.add((x2, y2))
    tile_q = next

while corner_q:
    x, y = corner_q.pop()
    requirements = (x > 0, y < col, x < row, y > 0)
    adjacent = ((x-1, y), (x, y+1), (x+1, y), (x, y-1))
    tile_pairs = ((x-1, x-1, y-1, y),  # up
                  (x-1, x, y, y),  # right
                  (x, x, y-1, y),  # down
                  (x-1, x, y-1, y-1))  # left
    for requirement, corner, tile_pair in zip(requirements, adjacent, tile_pairs):
        if requirement and corner not in visited and tile_pair not in pipes:
            visited.add(corner)
            corner_q.append(corner)

total = row * col - len(pipes)
for i in range(row):
    for j in range(col):
        corners = ((i, j), (i+1, j), (i, j+1), (i+1, j+1))
        if all(corner in visited for corner in corners):
            total -= 1

print(total)
