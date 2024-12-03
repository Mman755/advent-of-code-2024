import sys
import re

data = []
pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
for line in sys.stdin:
    for match in re.finditer(pattern, line):
        group = match.group()
        end_idx = match.end()
        if group.startswith("mul"):
            numbers = list(map(int, re.findall(r'\d+', group)))
            data.append((numbers, end_idx))
        elif group == "do()":
            data.append((True, end_idx))
        elif group == "don't()":
            data.append((False, end_idx))


can_compute, ans = True, 0
for op in data:
    first, idx = op
    if isinstance(first, bool) and isinstance(idx, int):
        can_compute = first
    elif isinstance(first, list) and isinstance(idx, int) and can_compute:
        ans += first[0] * first[1]
print(ans)



