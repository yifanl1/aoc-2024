import utils
from collections import defaultdict
import time

_s = time.time()

inp = utils.get_input(1)
rows = inp.split("\n")

c1 = []
c2 = []
freq = defaultdict(int)

for row in rows:
    if not row:
        continue
    r = row.split()
    c1.append(int(r[0]))
    c2.append(int(r[1]))
    freq[int(r[1])] += 1 

c1.sort()
c2.sort()

ans = 0
ans2 = 0
for i, a in enumerate(c1):
    ans += abs(a - c2[i])
    ans2 += a * freq.get(a, 0)
utils.write_output(ans, day=1, w=True, append=False)
utils.write_output(ans2, day=1, w=True, append=True)

_e = time.time()
utils.print_time_diff(_s, _e, 1)
