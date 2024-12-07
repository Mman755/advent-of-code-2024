import sys
from itertools import product

nums = []
targets = []
for line in sys.stdin:
    row = line.strip().split(":")
    targets.append(int(row[0]))
    nums.append(list(map(int, row[1].strip().split())))

data = list(zip(targets, nums))

ans = 0
for line in data:
    target, nums = line
    operators = list(product(['+', '*'], repeat=len(nums)-1))
    for ops in operators:
        res = nums[0]
        for i in range(len(ops)):
            if ops[i] == "+":
                res += nums[i + 1]
            else:
                res *= nums[i + 1]
        if res == target:
            ans += target
            break
print(ans)
