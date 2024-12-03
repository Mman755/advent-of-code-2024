import sys
import re

data = []
for line in sys.stdin:
    matches = re.findall(r"mul\(\d+,\d+\)", line)
    for match in matches:
        found = list(map(int, re.findall(r'\d+', match)))
        data.append(found)

ans = 0
for op in data:
    ans += op[0] * op[1]

print(ans)

