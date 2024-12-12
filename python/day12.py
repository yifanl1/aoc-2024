import utils
from collections import defaultdict

inp = utils.get_input(12)
sample_inp = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
# inp = sample_inp

DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))
neighbours = lambda c: set((c[0] + d[0], c[1] + d[1]) for d in DIRS)

def corners(region):
    # sides of a polygon == corners of a polygon
    ccount = 0
    for c in region:
        for i in range(len(DIRS)):
            d1, d2 = DIRS[i], DIRS[(i + 1) % 4]
            p1, p2 = (c[0] + d1[0], c[1] + d1[1]), (c[0] + d2[0], c[1] + d2[1])
            p3 = (p2[0] + d1[0], p2[1] + d1[1])
            # External Corner, examples: ..   .O
            #                            O.   O.
            if p1 not in region and p2 not in region:
                ccount += 1
            # Internal Corner, i.e. O.
            #                       OO
            elif p1 in region and p2 in region and p3 not in region:
                ccount += 1
    return ccount

rows = inp.strip().split()
plants = defaultdict(set)
for i, row in enumerate(rows):
    for j, p in enumerate(row):
        plants[p].add((i, j))

regions = []
for ptype, plst in plants.items():
    while plst:
        k = plst.pop()
        region = {k}
        candidates = neighbours(k) & plst
        plst -= candidates
        perim = 4
        while candidates:
            k_ = candidates.pop()
            perim += 4 - (2 * len(neighbours(k_) & region))
            region.add(k_)
            candidates = candidates | (neighbours(k_) & plst) - region
            plst -= candidates
        regions.append((frozenset(region), ptype, perim))

ans = ans2 = 0
ans = sum(len(x[0]) * x[2] for x in regions)
ans2 = sum(len(x[0]) * corners(x[0]) for x in regions)

utils.write_output(ans, day=12, w=1)
utils.write_output(ans2, day=12, a=1)