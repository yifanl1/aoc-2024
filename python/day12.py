import utils
from collections import defaultdict

TCoord = tuple[int, int]

inp: str = utils.get_input(12)
inp = """AAAAAAAAAA
ABBBBBBBBA
ABAAAAAAAA
ABABBBBBBB
ABABBBBBBB
ABABBBBBBB
AAABBBBBBB
CCCCCCCCCC
CCCCCCCCCC
CCCCCCCCCC
"""

DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))
neighbours = lambda c: set((c[0] + d[0], c[1] + d[1]) for d in DIRS)

def corners(region: set[TCoord]) -> int:
    """Counts corners of the region

    sides of a polygon == corners of a polygon
    . means cell is out of region, otherwise cell is in region
    looking upright from the bottom left, which of the following cases are corners?
    ..  ..  .C  .D  E.  F.  GG  HH
    A.  BB  C.  DD  E.  FF  G.  HH
    """
    ccount = 0
    for c in region:
        for i in range(len(DIRS)):
            d1, d2 = DIRS[i], DIRS[(i + 1) % 4]
            p1, p2 = (c[0] + d1[0], c[1] + d1[1]), (c[0] + d2[0], c[1] + d2[1])
            p3 = (p2[0] + d1[0], p2[1] + d1[1])
            if p1 not in region and p2 not in region:
                ccount += 1
            elif p1 in region and p2 in region and p3 not in region:
                ccount += 1
    return ccount

rows: list[str] = inp.strip().split()
plants: dict[str, set[TCoord]] = defaultdict(set)
for i, row in enumerate(rows):
    for j, p in enumerate(row):
        plants[p].add((i, j))

regions: list[tuple[set[TCoord], str, int]] = []
for ptype, pset in plants.items():
    while pset:
        k_ = pset.pop()
        region = {k_}
        candidates = set()
        perim = 4
        while candidates := candidates | (neighbours(k_) & pset) - region:
            pset -= candidates
            k_ = candidates.pop()
            perim += 4 - (2 * len(neighbours(k_) & region))
            region.add(k_)
        regions.append((frozenset(region), ptype, perim))

ans = ans2 = 0
ans = sum(len(x[0]) * x[2] for x in regions)
ans2 = sum(len(x[0]) * corners(x[0]) for x in regions)

utils.write_output(ans, day=12, w=1)
utils.write_output(ans2, day=12, a=1)