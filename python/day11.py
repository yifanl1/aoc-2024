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
    d = utils.int_len(stone)
    if d % 2 == 0:
        return stone // 10 ** (d // 2), stone % 10 ** (d // 2)
    return (stone * 2024,)

ctr = defaultdict(int)
for i in inp.strip().split():
    ctr[int(i)] += 1

for i in range(75):
    if i == 25:
        utils.write_output(ans, day=11, w=1)
    ans = 0
    new_ctr = defaultdict(int)
    for k, v in ctr.items():
        for k_ in stone_transform(k):
            new_ctr[k_] += v
            ans += v
    ctr = new_ctr

utils.write_output(ans, day=11, a=1)
_e = time.time()
utils.print_time_diff(_s, _e)
