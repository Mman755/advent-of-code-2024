import sys
from collections import defaultdict

map = []
for line in sys.stdin:
    map.append([item for item in line.strip()])

R, C = len(map), len(map[0])
antinodes = [["."] * C for _ in range(R)]

locations = defaultdict(list)
ans = 0
for row in range(R):
    for col in range(C):
        if map[row][col] != ".":
            locations[map[row][col]].append((row, col))

done, count = [], 0
for row in range(R):
    for col in range(C):
        if map[row][col] != ".":
            antennas = locations[map[row][col]]
            for i in range(len(antennas)):
                if antennas[i] == (row, col):
                    continue
                else:
                    done.append([antennas[i], (row, col)])
                curr_y, curr_x = row, col
                next_y, next_x = antennas[i]
                _dy, _dx  = curr_y - next_y, curr_x - next_x
                y_dir, x_dir = row + _dy, col + _dx

                while 0 <= y_dir < R and 0 <= x_dir < C: 
                    if antinodes[y_dir][x_dir] != "#":
                        antinodes[y_dir][x_dir] = "#"
                        count += 1
                    y_dir += _dy
                    x_dir += _dx

                y_dir, x_dir = row - _dy, col - _dx
                while 0 <= y_dir < R and 0 <= x_dir < C: 
                    if antinodes[y_dir][x_dir] != "#":
                        antinodes[y_dir][x_dir] = "#"
                        count += 1
                    y_dir -= _dy
                    x_dir -= _dx

print(count)
