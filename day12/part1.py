import sys

garden = []
for line in sys.stdin:
    garden.append(list(line.strip()))

R, C = len(garden), len(garden[0])
visited = set()

def flood_fill(y, x, target_crop, replacement):
    if (y < 0 or y >= R or x < 0 or x >= C or garden[y][x] != target_crop):
        return []

    coordinates = [(y, x)]
    garden[y][x] = replacement
    for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        dy, dx = dir
        coordinates += flood_fill(y + dy, x + dx, target_crop, replacement)

    return coordinates

def calculate_perimeter(grid, group_coordinates):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    perimeter = 0

    for row, col in group_coordinates:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) not in group_coordinates:
                perimeter += 1
    return perimeter

ans = 0
for row in range(R):
    for col in range(C):
        if (row, col) not in visited:
            coordinates = flood_fill(row, col, garden[row][col], '*')
            ans += len(coordinates) * calculate_perimeter(garden, coordinates)
            for c in coordinates:
                visited.update(c for c in coordinates)
print(ans)
