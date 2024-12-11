from collections import deque
input = """27 10647 103 9 0 5524 4594227 902936"""

stones = deque([int(x) for x in input.strip().split()])

blinks = 25
while blinks > 0:
    queue_len = len(stones)
    for _ in range(queue_len):
        stone = stones.popleft()
        stone_str = str(stone)
        if stone == 0:
            stones.append(1)
        elif len(stone_str) % 2 == 0:
            mid = len(stone_str) // 2
            first, second = int(stone_str[:mid]), int(stone_str[mid:])
            stones.extend([first, second])
        else:
            stones.append(stone * 2024)
    blinks -= 1
print(len(stones))

