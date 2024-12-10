import sys
from functools import lru_cache

grid = []
for line in sys.stdin:
    grid.append([int(char) for char in line.strip().split()[0]])

R, C = len(grid), len(grid[0])

def dfs(row, col, visited):
    if row < 0 or row >= R or col < 0 or col >= C or (row, col) in visited:
        return set()
    if grid[row][col] == 9:
        return {(row, col)}
    visited.add((row, col))

    reached = set()
    for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        ny, nx = row + dy, col + dx
        if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == grid[row][col] + 1:
            reached |= dfs(ny, nx, visited)
    return reached

ans = 0
for row in range(R):
    for col in range(C):
        if grid[row][col] == 0:
            visited = set()
            ans += len(dfs(row, col, visited))
print(ans)
