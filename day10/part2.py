import sys

grid = []
for line in sys.stdin:
    grid.append([int(char) for char in line.strip().split()[0]])

R, C = len(grid), len(grid[0])

def dfs(row, col, visited):
    if row < 0 or row >= R or col < 0 or col >= C or (row, col) in visited:
        return 0
    if grid[row][col] == 9:
        return 1
    visited.add((row, col))

    total_paths = 0
    for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        ny, nx = row + dy, col + dx
        if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == grid[row][col] + 1:
            total_paths += dfs(ny, nx, visited)

    visited.remove((row, col))
    return total_paths

ans = 0
for row in range(R):
    for col in range(C):
        if grid[row][col] == 0:
            visited = set()
            ans += dfs(row, col, visited)
print(ans)

