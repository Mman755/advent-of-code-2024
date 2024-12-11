import sys
from functools import lru_cache

# Replaced part 1 with part 2 memo sol
@lru_cache(None)
def blink(stone, iters):
    if iters == 0:
        return 1

    if stone == 0:
        return blink(1, iters - 1)

    elif len(str(stone)) % 2 == 0:
        length = len(str(stone))
        first, second = int(str(stone)[:length // 2]), int(str(stone)[length // 2:])
        return blink(first, iters - 1) + blink(second, iters - 1)

    return blink(stone * 2024, iters - 1)

def solve(stones, iterations):
    return sum([blink(stone, iterations) for stone in stones])

stones = [int(stone) for stone in sys.stdin.readline().split(" ")]
print(solve(stones, 75))
