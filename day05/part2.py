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
            updates.append(list(map(int, line.strip().split(","))))

ans = 0
wrong_lines = []
for update_line in updates:
    valid = True
    for i in range(len(update_line)):
        prefix, postfix = update_line[:i], update_line[i + 1:]
        all_before = [num for num in prefix if num in after_mapping[update_line[i]]]
        all_after = [num for num in postfix if num in before_mapping[update_line[i]]]
        valid = len(all_before) == 0 and len(all_after) == 0
        if not valid:
            wrong_lines.append(update_line)
            break


for idx, wrong_line in enumerate(wrong_lines):
    new_line = []
    remaining = set(wrong_line)  
    while remaining:
        for num in list(remaining):
            before_count = len([x for x in before_mapping[num] if x in remaining])
            if before_count == 0:
                new_line.append(num)
                remaining.remove(num)

    ans += new_line[len(new_line) // 2]

print(ans)
