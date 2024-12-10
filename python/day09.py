import utils
import time

_s = time.time()

inp = utils.get_input(9)
sample_inp = "2333133121414131402"
# inp = sample_inp

def insort(lst, v):
    for i, v_ in enumerate(lst):
        if v_ > v:
            lst.insert(i, v)
            break
    else:
        lst.append(v)

free = []
free_blocks, filled, blocks = {}, {}, {}

pos = 0
for i, l in enumerate(inp.strip()):
    l = int(l)
    if i % 2:
        if l:
            free.extend(range(pos, pos + l))
            free_blocks[pos] = l
    else:
        # Storing the file blocks in the order we'll be retrieving them for ease
        filled[i // 2] = list(range(pos + l - 1, pos - 1, -1))
        blocks[i // 2] = pos, l
    pos += l
fbk = list(sorted(free_blocks.keys()))
free = free[::-1]

ans = ans2 = 0
seen = set()
# Logically, if there are X input characters, 
#   the highest pid will be X/2 - 1 due to alternation + zero indexing
for pid in range(len(inp) // 2 - 1, -1, -1):
    # part 1
    for k in filled[pid]:
        k_ = k
        if free and free[-1] < k:
            k_ = free[-1]
            free.pop()
        ans += k_ * pid

    # part 2
    s, l = blocks[pid]
    for k in fbk:
        if k >= s:
            ans2 += utils.rsum(s, s + l) * pid
            break
        l2 = free_blocks[k]
        if l2 < l:
            continue
        del free_blocks[k]
        fbk.remove(k)
        if l2 > l:
            free_blocks[k + l] = l2 - l
            insort(fbk, k + l)
        ans2 += utils.rsum(k, k + l) * pid
        break
utils.write_output(ans, day=9, w=1)
utils.write_output(ans2, day=9, a=1)

_e = time.time()
utils.print_time_diff(_s, _e)