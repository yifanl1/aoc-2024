import utils
import time

_s = time.time()

inp = utils.get_input(9)
sample_inp = "2333133121414131402"
# inp = sample_inp
# inp = "12143"
inp="121012121010121010121212121012121010121010121212"

def insort(lst, v):
    for i, v_ in enumerate(lst):
        if v_ > v:
            lst.insert(i, v)
            break
    else:
        lst.append(v)

free = []
free_blocks, file_blocks = {}, {}

idx = 0
mpid = -1
for i in range(len(inp.strip())):
    l = int(inp[i])
    if i % 2:
        if l:
            free.extend(range(idx, idx + l))
            free_blocks[idx] = l
    else:
        file_blocks[i // 2] = idx, l
        mpid += 1
    idx += l
# accessing last element of a list is much faster than accessing first
free = free[::-1]
s_fbk = sorted(free_blocks.keys())

ans = ans2 = 0
for pid in range(mpid, -1, -1):
    s, l = file_blocks[pid]
    # part 1
    for i in range(l - 1, -1, -1):
        k_ = s + i
        if free and free[-1] < k_:
            k_ = free[-1]
            free.pop()
        ans += k_ * pid

    # part 2
    for k in s_fbk:
        if k >= s:
            ans2 += utils.rsum(s, s + l) * pid
            break
        l2 = free_blocks[k]
        if l2 < l:
            continue
        del free_blocks[k]
        s_fbk.remove(k)
        if l2 > l:
            free_blocks[k + l] = l2 - l
            insort(s_fbk, k + l)
        ans2 += utils.rsum(k, k + l) * pid
        break
    else:
        ans2 += utils.rsum(k, k + l) * pid
utils.write_output(ans, day=9, w=1)
utils.write_output(ans2, day=9, a=1)

_e = time.time()
utils.print_time_diff(_s, _e)