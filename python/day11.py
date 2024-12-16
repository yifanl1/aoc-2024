import utils
from collections import defaultdict
import time
_s = time.time()

inp = utils.get_input(11)
sample_inp = "1 0 1 0 1 0\n"
# inp = sample_inp
inp = "1950139 0 3 837 6116 18472 228700 45 \n"

def stone_transform(stone: int, memo) -> tuple[int, ...]:
    try:
        return memo[stone]
    except KeyError:
        ret = (stone * 2024,)
        d = utils.int_len(stone)
        if d % 2 == 0:
            ret = divmod(stone, 10 ** (d // 2))
        memo[stone] = ret
        return ret

_MEMO = {0: (1,)}

def iterate(inp: str, n: int):
    ctr = defaultdict(int)
    for i in inp.strip().split():
        ctr[int(i)] += 1

    for i in range(n):
        ctr_ = defaultdict(int)
        for k, v in ctr.items():
            for k_ in stone_transform(k, _MEMO):
                ctr_[k_] += v
        ctr = ctr_
    return sum(ctr.values())

ans = iterate(inp, 25)
ans2 = iterate(inp, 75)
utils.write_output(ans, day=11, w=1)
utils.write_output(ans2, day=11, a=1)

# print(iterate(inp, 1000))

_e = time.time()
utils.print_time_diff(_s, _e)

# 218574552533883380465768547080900751287565254595747066069904430752026115021538325803593129385619328285668771739366033629529881924216367072403222706107610718635751139861009755749128409