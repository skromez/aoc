from collections import defaultdict
import heapq

input = """
2333133121414131402
"""

input = [int(char) for char in input.strip()]

disk = []
fid = 0

for i, x in enumerate(input):
    if i % 2 == 0:
        disk += [fid] * x
        fid += 1
    else:
        disk += [-1] * x
blanks = [i for i, x in enumerate(disk) if x == -1]

for i in blanks:
    while disk[-1] == -1: disk.pop()
    if len(disk) <= i: break
    disk[i] = disk.pop()

print(sum(i * x for i, x in enumerate(disk)))