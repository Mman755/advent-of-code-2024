import sys
import re

positions, velocities = [], []
for line in sys.stdin:
    numbers = re.findall(r'-?\d+', line)
    positions.append([int(numbers[0]), int(numbers[1])])
    velocities.append([int(numbers[2]), int(numbers[3])])

R, C = 103, 101

space = [[0 for _ in range(C)] for _ in range(R)]

for pair in positions:
    x, y = pair[0], pair[1]
    space[y][x] = 1 if space[y][x] == 0 else space[y][x] + 1

visited = set()
def dfs(y, x, matrix):
    if not (0 <= y < R and 0 <= x < C) or (y, x) in visited or matrix[y][x] == 0:
        return 0
    visited.add((y, x))
    size = 1

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        size += dfs(y + dy, x + dx, matrix)

    return size

STEP_HEURISTIC = 10000
DFS_HEURISTIC = 5000 # Adjust heuristic (The easter egg always shows sometime after 5000 seconds though)
cnctd_comps = []
for i in range(STEP_HEURISTIC):
    for idx, pos in enumerate(positions):
        x, y = pos[0], pos[1]
        vel = velocities[idx]
        vx, vy = vel[0], vel[1]

        dx, dy = (x + vx) % C, (y + vy) % R
        space[y][x] -= 1
        space[dy][dx] += 1
        positions[idx][0], positions[idx][1] = dx, dy

        if i >= DFS_HEURISTIC: 
            cnctd_comps.append((i, dfs(dy, dx, space)))
    visited.clear()

sorted_components = sorted(cnctd_comps, key = lambda x: x[1])
print(sorted_components[-1][0])
