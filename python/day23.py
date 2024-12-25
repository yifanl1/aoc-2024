import utils
from collections import defaultdict
import itertools as it
import time

_s = time.time()

inp = utils.get_input(23)
# inp = utils.get_input(23, pathoverride="23sample")

rows = inp.strip().split("\n")
map_ = defaultdict(set)
for row in rows:
    l, r = row.split("-", maxsplit=1)
    map_[l].add(r)
    map_[r].add(l)

interconnected = set()
for k1, v in map_.items():
    # print("*" * 80)
    # print(k1, v)
    for k2 in v:
        for k3 in v & map_[k2]:
            interconnected.add(tuple(sorted([k1, k2, k3])))
            # print("||", k3, map_[k3], inter_)

# Thanks wikipedia!
def BK2(R: set[str], P: set[str], X: set[str]) -> set[str]:
    if not (P or X):
        return {",".join(list(sorted(R)))}
    ret = set()

    u = (P | X).pop()
    P_ = P - map_[u]
    while P_:
        v = P_.pop()
        X |= {v}
        ret |= BK2(R | {v}, P & map_[v], X & map_[v])
    return ret

def BK1(R: set[str], P: set[str], X: set[str]) -> set[str]:
    if not (P or X):
        return {",".join(list(sorted(R)))}
    ret = set()

    while P:
        v = P.pop()
        X |= {v}
        ret |= BK1(R | {v}, P & map_[v], X & map_[v])
    return ret

all_cliques = BK2(set(), set(map_.keys()), set())

best = sorted(all_cliques, key=len, reverse=1)[0]
ans = sum(any(s[0] == "t" for s in c) for c in interconnected)
utils.write_output(ans, 23, w=1)
utils.write_output(best, 23, a=1)

_e = time.time()
utils.print_time_diff(_s, _e, 23)