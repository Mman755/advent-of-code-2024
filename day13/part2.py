import sys
import re

OFFSET = 10000000000000

buttons = [[]]
curr = 0
for line in sys.stdin:
    numbers = re.findall(r'\d+', line)
    if len(numbers) == 2:
        x, y = int(numbers[0]), int(numbers[1])
        buttons[curr].append((x, y))
    else:
        curr += 1
        buttons.append([])

ans = 0
for button in buttons:
    a1, b1, a2, b2 = button[0][0], button[1][0], button[0][1], button[1][1],   
    xe, ye = button[2][0] + OFFSET, button[2][1] + OFFSET

    b = ((a2 * xe) - (a1 * ye)) / ((a2 * b1) - (a1 * b2))
    a = (ye - (b2 * b)) / a2

    if a.is_integer() and b.is_integer(): ans += (3 * a) + b

print(int(ans))
