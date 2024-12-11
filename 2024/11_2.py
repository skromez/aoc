from collections import deque
from functools import cache

input = """27 10647 103 9 0 5524 4594227 902936"""

stones = [int(x) for x in input.strip().split()]

@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps - 1)
    string = str(stone)
    length = len(string)
    if length % 2 == 0:
        return count(int(string[:length // 2]), steps - 1) + count(int(string[length // 2:]), steps - 1)
    return count(stone * 2024, steps - 1)

print(sum(count(stone, 75) for stone in stones))# 