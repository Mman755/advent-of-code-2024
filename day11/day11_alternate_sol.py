import sys
from collections import defaultdict, Counter

def blink(stones):
    transformed = defaultdict(int)
    for stone, sc in stones.items():
        if stone == 0: transformed[1] += sc

        elif len(str(stone)) % 2 == 0:
            length = len(str(stone))
            first, second = int(str(stone)[:length // 2]), int(str(stone)[length // 2:])
            transformed[first] += sc
            transformed[second] += sc

        else: transformed[stone * 2024] += sc

    return transformed

def solve(N, stones):
    stone_counts = Counter(stones)
    for _ in range(N):
         stone_counts = blink(stone_counts)

    return sum(stone_counts.values())

stones = [int(stone) for stone in sys.stdin.readline().split(" ")]

print(solve(25, stones)) # Part 1
print(solve(75, stones)) # Part 2
