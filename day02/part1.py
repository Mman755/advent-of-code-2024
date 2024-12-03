import sys

data = []
for line in sys.stdin:
    line = line.strip().split()
    report = [int(char) for char in line]
    data.append(report)

def check_safety(report):
    N = len(report)
    is_constant = (all(report[i] < report[i + 1] for i in range(N - 1)) or
    all(report[i] > report[i + 1] for i in range(N - 1)))

    max_difference = 0
    for i in range(1, N):
        max_difference = max(max_difference, abs(report[i] - report[i - 1]))

    return (is_constant, max_difference)


N = len(data)

safe_reports = 0
for i in range(N):
    is_sorted, level_diff = check_safety(data[i])
    if is_sorted and (1 <= level_diff <= 3):
        safe_reports += 1

print(safe_reports)
