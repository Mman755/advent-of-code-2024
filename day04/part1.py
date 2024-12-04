import sys

data = []
for line in sys.stdin:
    process = line.strip()
    data.append([char for char in process])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
R, C = len(data), len(data[0])
search = "XMAS"

ans = 0
for row in range(R):
    for col in range(C):
        for dy, dx in directions: 
            word = ""
            r, c = row, col
            for i in range(4):
                if 0 <= r < R and 0 <= c < C:
                    word += data[r][c]
                    r += dy
                    c += dx
            if word == search:
                ans += 1

print(ans)
