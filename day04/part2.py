import sys
from collections import Counter

data = []
for line in sys.stdin:
    process = line.strip()
    data.append([char for char in process])

directions = [(1, 1), (1, -1)]
R, C = len(data), len(data[0])
search = "MAS"

ans = 0
for row in range(R):
    for col in range(C):
        first, second = "", ""
        r, c = row, col
        for i in range(3):
            if 0 <= r < R and 0 <= c < C:
                first += data[r][c]
                r += 1
                c += 1
        r, c = row, col + 2
        for i in range(3):
            if 0 <= r < R and 0 <= c < C:
                second += data[r][c]
                r += 1
                c += -1
        if (first == search or first[::-1] == search) and (second == search or second[::-1] ==
                                                           search):
            ans += 1

print(ans)
