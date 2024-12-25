import utils
from collections import deque, Counter
import time

_s = time.time()

inp = utils.get_input(22)

# 16777216 = 2 ** 24
# so mod 2 ** 24 is the same as taking the last 23 bits!
PRUNE = (1 << 24) - 1

def secret(v, psum, n=1):
    i = 0
    seq = (None, None, None, None)
    seen = {}
    for i in range(n):
        v_ = (v ^ (v << 6)) & PRUNE
        v_ = (v_ ^ (v_ >> 5)) & PRUNE
        v_ = (v_ ^ (v_ << 11)) & PRUNE
        p, d = v_ % 10, (v_ % 10 - v % 10)
        v = v_

        seq = (*seq[1:], d)
        # Greed is good
        if d > 0 and i >= 3 and seq not in seen:
            psum[seq] += p
            seen[seq] = p
    return v, seen

allsecrets = 0
all_maps = []
psum = Counter()
all_maps = []
for row in inp.strip().split("\n"):
    v_, pmap = secret(int(row), psum, 2000)
    allsecrets += v_
    all_maps.append(pmap)
bananamax = max(psum.values())

utils.write_output(allsecrets, 22, w=1)
utils.write_output(bananamax, 22, a=1)

_e = time.time()

utils.print_time_diff(_s, _e, day=22)