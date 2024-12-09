import utils

inp = utils.get_input(9)
sample_inp = "2333133121414131402"
# inp = sample_inp
# inp = "12121"

pid = 0
free = set()
free_blocks = {}
filled = {}
blocks = {}
pos = 0
for i, l in enumerate(inp.strip()):
    l = int(l)
    if i % 2:
        if l:
            free |= set(range(pos, pos + l))
            free_blocks[pos] = l
    else:
        for j in range(pos, pos + l):
            filled[j] = pid
        blocks[pid] = pos, l
        pid += 1
    pos += l

while True:
    k = max(filled.keys())
    m = min(free)
    if m > k:
        break
    v = filled[k]
    del filled[k]
    free -= {m}
    filled[m] = v
ans = 0
for k, v in filled.items():
    ans += (k * v)
utils.write_output(ans, day=9, w=1)

new_filled = {}
for pid in sorted(blocks.keys(), key=lambda x: -x):
    s, l = blocks[pid]
    for k2 in sorted(free_blocks.keys()):
        if k2 > s:
            continue
        if free_blocks[k2] < l:
            continue
        l2 = free_blocks[k2]
        del free_blocks[k2]
        if l2 > l:
            free_blocks[k2 + l] = (l2 - l)
        for i in range(k2, k2 + l):
            assert i not in new_filled
            new_filled[i] = pid
        break
    else:
        for i in range(s, s + l):
            assert i not in new_filled
            new_filled[i] = pid
ans = 0
# print(new_filled)
for k, v in new_filled.items():
    ans += (k * v)
utils.write_output(ans, day=9, a=1)