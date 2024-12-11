import utils
from collections import defaultdict
import time
_s = time.time()

inp = utils.get_input(11)
sample_inp = "125 17\n"
# inp = sample_inp

def stone_transform(stone: int) -> tuple[int, ...]:
    if stone == 0:
        return (1,)
    l = len(str(stone))
    if l % 2 == 0:
        r, l = int(str(stone)[:l // 2]), int(str(stone)[l // 2:])
        return r, l
    return (stone * 2024,)

ctr = defaultdict(int)
for i in inp.strip().split():
    ctr[int(i)] += 1

CUTOFFS = (24, 74)
for i in range(500):
    ans = 0
    new_ctr = defaultdict(int)
    for k, v in ctr.items():
        for k_ in stone_transform(k):
            new_ctr[k_] += v
            ans += v
    ctr = new_ctr
    if i == CUTOFFS[0]:
        utils.write_output(ans, day=11, w=1)
    if i == CUTOFFS[1]:
        utils.write_output(ans, day=11, a=1)
    print(i + 1, ans)

_e = time.time()
utils.print_time_diff(_s, _e)