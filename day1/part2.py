import sys

data = []
for line in sys.stdin:
    line = line.strip().split()
    data.append(line)

first_list = []
freq = {}

for line in data:
    first_list.append(int(line[0]))
    freq[int(line[1])] = freq.get(int(line[1]), 0) + 1

similarity = 0
for i in range(len(first_list)):
    similarity += first_list[i] * freq.get(first_list[i], 0)

print(similarity)
