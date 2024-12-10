import sys

data = [int(char) for char in sys.stdin.readline().strip()]
N = len(data)
layout = []

idx = 0
for i in range(N):
    if i % 2 == 0:
        layout.extend([idx for _ in range(data[i])])
        idx += 1
    else:
        layout.extend(["." for _ in range(data[i])])

del idx, data
free_ptr = next(i for i, val in enumerate(layout) if val == ".")
right = len(layout) - 1
while free_ptr <= right:
    if layout[right] != ".":
        layout[free_ptr], layout[right] = layout[right], "."
        right -= 1
        while layout[free_ptr] != ".": free_ptr += 1
    else: right -= 1

ans = sum(_idx * x for _idx, x in enumerate(layout) if x != ".")
print(ans)
