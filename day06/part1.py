import sys

grid = []
for line in sys.stdin:
    grid.append([pt for pt in line.strip()])

R, C = len(grid), len(grid[0])

start_pos = (0, 0)
for row in range(R):
    for col in range(C):
        if grid[row][col] == "^":
            start_pos = (row, col)
            break

i, j = start_pos[0], start_pos[1]
marked = [row[:] for row in grid]
 
dir = {"^" : ">", ">" : "v", "v" : "<", "<" : "^"}
dist = {"^" : (-1, 0), ">" : (0, 1), "v" : (1, 0), "<" : (0, -1)}

while True:
    try:
        loc = grid[i][j]
        change_dist = dir[loc]
        dy, dx = dist[loc]
        while grid[i + dy][j + dx] == ".":
            marked[i][j] = "X"
            grid[i][j] = "."
            i += dy
            j += dx
            grid[i][j] = loc
            marked[i][j] = "X"
            by, bx = i + dy, j + dx
            if grid[i + dy][j + dx] == "#":
                grid[i][j] = change_dist

        if (by < 0 or by >= R) or (bx < 0 or bx >= C):
            break
    except IndexError:
        break

ans = 0
for row in marked:
    for loc in row:
        if loc == "X": ans += 1

print(ans)
