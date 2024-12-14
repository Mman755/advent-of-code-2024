import sys
import copy

garden = []
for line in sys.stdin:
    garden.append(list(line.strip()))

original_garden = copy.deepcopy(garden)
R, C = len(garden), len(garden[0])
visited = set()

def fill(y, x, target_crop, replacement):
    if (y < 0 or y >= R or x < 0 or x >= C or garden[y][x] != target_crop):
        return []

    coordinates = [(y, x)]
    garden[y][x] = replacement
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dir in dirs:
        dy, dx = dir
        coordinates += fill(y + dy, x + dx, target_crop, replacement)

    return coordinates

def find_corners(coords):
    corners = 0
    for edge in coordinates:
        y, x = edge
        # Convex corners
        if (y - 1, x) not in coords and (y, x - 1) not in coords: corners += 1
        if (y - 1, x) not in coords and (y, x + 1) not in coords: corners += 1
        if (y + 1, x) not in coords and (y, x - 1) not in coords: corners += 1
        if (y + 1, x) not in coords and (y, x + 1) not in coords: corners += 1

        # Concave corners
        if (y, x + 1) in coords and (y + 1, x) in coords and (y + 1, x + 1) not in coords: corners += 1
        if (y, x - 1) in coords and (y - 1, x) in coords and (y - 1, x - 1) not in coords: corners += 1
        if (y, x - 1) in coords and (y + 1, x) in coords and (y + 1, x - 1) not in coords: corners += 1
        if (y, x + 1) in coords and (y - 1, x) in coords and (y - 1, x + 1) not in coords: corners += 1

    return corners

ans = 0
for row in range(R):
   for col in range(C):
       if (row, col) not in visited and garden[row][col] != "*":
            coordinates = fill(row, col, garden[row][col], '*')
            ans += len(coordinates) * find_corners(coordinates)
            for c in coordinates:
                visited.update(c for c in coordinates)
print(ans)
