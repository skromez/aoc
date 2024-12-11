from collections import Counter
from functools import cache

input = """27 10647 103 9 0 5524 4594227 902936"""

stones = [int(x) for x in input.strip().split()]

count = Counter(stones)

for _ in range(75):
    ncount = Counter()

    for x in count.keys():
        c = count[x]
        if x == 0:
            ncount[1] += c
        elif len(str(x)) % 2 == 0:
            s = str(x)
            lx, rx = s[:len(s) // 2], s[len(s) // 2:]
            ncount[int(lx)] += c
            ncount[int(rx)] += c
        else:
            ncount[x * 2024] += c
    count = ncount
print(sum(count.values()))