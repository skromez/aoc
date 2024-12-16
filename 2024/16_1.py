input = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

from heapq import heappush, heappop
grid = [list(row) for row in input.strip().split('\n')]

rows = len(grid)
cols = len(grid[0])
start = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start = (0, r, c, (0, 1))
            break
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
q = [(start)]
seen = set()
paths = []
while q:
    weight, cr, cc, (cdr, cdc) = heappop(q)
    if (cr, cc, (cdr, cdc)) in seen: continue
    if cr < 0 or cc < 0 or cr >= rows or cc >= cols: continue

    seen.add((cr, cc, (cdr, cdc)))
    if grid[cr][cc] == 'E':
        paths.append((weight, cr, cc))
        continue
    if grid[cr][cc] == '#': continue
    for dr, dc in directions:
        nr, nc = cr + dr, cc + dc
        new_weight = weight + (1 if (dr, dc) == (cdr, cdc) else 1001)
        heappush(q, (new_weight, nr, nc, (dr, dc)))
print(min(paths))