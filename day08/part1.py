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
                if 0 <= row + _dy < R and 0 <= col + _dx < C: 
                    if antinodes[row + _dy][col + _dx] != "#":
                        count += 1
                        antinodes[row + _dy][col + _dx] = "#"
print(count)
