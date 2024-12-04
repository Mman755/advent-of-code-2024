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
        r1, c1 = row, col + 2
        for i in range(3):
            if 0 <= r < R and 0 <= c < C:
                first += data[r][c]
                r += 1
                c += 1
            if 0 <= r1 < R and 0 <= c1 < C:
                second += data[r1][c1]
                r1 += 1
                c1 += -1

        if (first == search or first[::-1] == search) and (second == search or second[::-1] ==
                                                           search):
            ans += 1

print(ans)
