import utils
import time

_s = time.time()

inp = utils.get_input(19)

_d, _c = inp.strip().split("\n\n", maxsplit=1)
designs = set(_d.split(", "))
candidates = _c.split("\n")
DMAP = {}

for c in "wubrg":
    DMAP[c] = [(d, len(d)) for d in designs if d[0] == c]

_MEMO = {"": 1}
def composition_cnt(candidate):
    if candidate in _MEMO:
        return _MEMO[candidate]
    cnt = 0
    for d, l in DMAP[candidate[0]]:
        if not candidate[:l] == d:
            continue
        cnt += composition_cnt(candidate[l:])
    _MEMO[candidate] = cnt
    return cnt

ans = sum(map(bool, map(composition_cnt, candidates)))
utils.write_output(ans, day=19, w=1)
ans2 = sum(map(composition_cnt, candidates))
utils.write_output(ans2, day=19, a=1)

_e = time.time()
utils.print_time_diff(_s, _e)
