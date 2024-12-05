import sys
from collections import defaultdict

before_mapping = defaultdict(set)
after_mapping = defaultdict(set)
updates = []
for line in sys.stdin:
    if "|" in line.strip():
        row = line.strip().split("|")
        a, b = int(row[0]), int(row[1])
        after_mapping[a].add(b)
        before_mapping[b].add(a)
    else:
        if line.strip():
            row = line.strip().split(",")
            updates.append(list(map(int, row)))

ans = 0
for update_line in updates:
    valid = True
    for i in range(len(update_line)):
        prefix, postfix = update_line[:i], update_line[i + 1:]
        all_before = len([num for num in prefix if num in after_mapping[update_line[i]]]) == 0
        all_after = len([num for num in postfix if num in before_mapping[update_line[i]]]) == 0
        valid = all_before and all_after
        if not valid: break
    if valid:
        ans += update_line[(len(update_line)) // 2]

print(ans)
