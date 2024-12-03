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

    max_difference = all(1 <= abs(report[i] - report[i - 1]) <= 3 for i in range(1, N))

    return is_constant and max_difference


N = len(data)
safe_reports = 0
for i in range(N):
    is_safe = check_safety(data[i])
    if is_safe: safe_reports += 1
    else:
        report = data[i]
        for j in range(N):
            is_safe = check_safety(report[: j] + report[j + 1 : ])
            if is_safe:
                safe_reports += 1
                break

print(safe_reports)
