import utils
from collections import defaultdict

TCoord = complex

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

DIRS = (-1, 1j, 1, -1j)
neighbours = lambda c: set(c + d for d in DIRS)

def corners(region: set[TCoord]) -> int:
    # sides of a polygon == corners of a polygon
    ccount = 0
    for c in region:
        for i in range(len(DIRS)):
            d1, d2 = DIRS[i], DIRS[(i + 1) % 4]
            p1, p2, p3 = c + d1, c + d2, c + d1 + d2
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
plants: dict[str, set[TCoord]] = defaultdict(set)
for i, row in enumerate(rows):
    for j, p in enumerate(row):
        plants[p].add(i + j * 1j)

regions: list[tuple[set[TCoord], str, int]] = []
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