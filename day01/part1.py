import sys

data = []
for line in sys.stdin:
    line = line.strip().split()
    data.append(line)

first_list, second_list = [], []

for line in data:
    first_list.append(int(line[0]))
    second_list.append(int(line[1]))

first_list.sort()
second_list.sort()

distance = 0
for i in range(len(first_list)):
    distance += abs(first_list[i] - second_list[i])

print(distance)
