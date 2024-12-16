import sys
import re

PART_ONE_SECONDS = 100

positions = []
velocities = []
for line in sys.stdin:
    numbers = re.findall(r'-?\d+', line)
    positions.append([int(numbers[0]), int(numbers[1])])
    velocities.append([int(numbers[2]), int(numbers[3])])

R, C = 103, 101

space = [[0 for _ in range(C)] for _ in range(R)]

for pair in positions:
    x, y = pair[0], pair[1]
    space[y][x] = 1 if space[y][x] == 0 else space[y][x] + 1

for _ in range(PART_ONE_SECONDS):
    for idx, pos in enumerate(positions):
        x, y = pos[0], pos[1]
        vel = velocities[idx]
        vx, vy = vel[0], vel[1]

        dx, dy = (x + vx) % C, (y + vy) % R
        space[y][x] -= 1
        space[dy][dx] += 1

        positions[idx][0], positions[idx][1] = dx, dy


mid_row, mid_col = R // 2, C // 2

top_left = [[space[j][i] for i in range(mid_col)] for j in range(mid_row)]
top_right = [[space[j][i] for i in range(mid_col + 1, C)] for j in range(mid_row)]
bottom_left = [[space[j][i] for i in range(mid_col)] for j in range(mid_row + 1, R)]
bottom_right = [[space[j][i] for i in range(mid_col + 1, C)] for j in range(mid_row + 1, R)]

ans = (
        sum(sum(row) for row in top_left) *
        sum(sum(row) for row in top_right) * 
        sum(sum(row) for row in bottom_left) * 
        sum(sum(row) for row in bottom_right)
       )

print(ans)
