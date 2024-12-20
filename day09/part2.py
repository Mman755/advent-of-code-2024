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
        layout.extend([-1 for _ in range(data[i])])

def block_window(right_ptr, layout):
    starting_ptr = right_ptr
    while starting_ptr >= 0 and layout[starting_ptr] == layout[right_ptr]:
        starting_ptr -= 1
    return (starting_ptr + 1, right_ptr)

def get_available_windows(right, layout):
    N = right
    coords = []
    i = 0
    while i < N:
        if layout[i] == -1:
            start = i
            while i < N and layout[i] == -1: i += 1
            coords.append((start, i - 1))
        else: i += 1
    return coords

del idx, data
free_ptr = next(i for i, val in enumerate(layout) if val == -1)
right = len(layout) - 1
while free_ptr <= right:
    free_spaces = get_available_windows(right, layout)
    block_start, block_end = block_window(right, layout)
    block_size = block_end - block_start + 1

    for idx, space in enumerate(free_spaces):
        sl, sr = space
        if (sr - sl + 1) >= block_size:
            for i in range(sl, sl + block_size):
                layout[i] = layout[right]
                layout[right] = -1
                right -= 1

            free_ptr = next(i for i, val in enumerate(layout) if val == -1)
            del free_spaces[idx]
            right = block_start
            break
    char = layout[right]
    while layout[right] == char or layout[right] == -1: 
        right -= 1

ans = sum(_idx * x for _idx, x in enumerate(layout) if x != -1)
print(ans)
