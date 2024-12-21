import utils
from collections import deque
import time

_s = time.time()

def op_(program: list[int], regs: list[int, int, int], ptr: int, outbuf: list[int]) -> int:
    assert ptr + 1 < len(program)
    ptr_ = ptr + 2
    opcode, operand = program[ptr], program[ptr + 1]
    c_operand = coperand(operand, regs)
    match opcode:
        case 0: # adv
            regs[0] = regs[0] >> c_operand
        case 1: # bxl
            regs[1] = regs[1] ^ operand
        case 2: # bst
            regs[1] = c_operand & 0b111
        case 3: # jnz
            if regs[0]:
                ptr_ = operand
        case 4: # bxc
            regs[1] = regs[1] ^ regs[2]
        case 5: # out
            outbuf.append(c_operand & 0b111)
        case 6: # bdv
            regs[1] = regs[0] >> c_operand
        case 7: # cdv
            regs[2] = regs[0] >> c_operand
        case _:
            raise ValueError("Evil is happening")
    return ptr_

def coperand(operand: int, regs: list[int, int, int]) -> int:
    # assert operand in (0, 1, 2, 3, 4, 5, 6)
    return operand if operand <= 3 else regs[operand - 4]

def run_program(program: list[int], regs: list[int, int, int]) -> list[int]:
    outbuf = []
    ptr = 0
    end = len(program)
    while ptr < end:
        ptr = op_(program, regs, ptr, outbuf)
    return outbuf


inp = utils.get_input(17)
rows = inp.strip().split("\n")
regs = list(map(int, (rows[i].split()[-1] for i in range(3))))
program = list(map(int, rows[-1].split(maxsplit=1)[1].split(",")))
outbuf = run_program(program, regs)
utils.write_output(",".join(map(str, outbuf)), 17, w=1)

"""
B = A % 8         # bst 4
B = B ^ _         # bxl _
C = A >> B        # cdv 5
B = B ^ _         # bxl _
B = B ^ C         # bxc 3
out B % 8         # out 5
A = A // 8        # adv 3
JNZ 0

Insight 1: Every output digit sorta corresponds to 1 base 8 digit for A in reverse order
Insight 2: B and C immediately get overwritten based on A, they don't really matter

Problem: not a simple function of single base 8 digits mapping :/
Accumulate values?
"""
def quineify(program: list[int]) -> int:
    candidates = deque([(program, len(program) - 1, 0, ())])
    while candidates:
        program, offset, val, digitacc = candidates.popleft()
        for test in range(8):
            val_ = (val * 8) + test
            regs = [val_, 0 ,0]
            if run_program(program, regs) == program[offset:]:
                # print(offset, test, digitacc)
                if offset == 0:
                    return val_ 
                candidates.append((program, offset - 1, val_, (test, *digitacc)))
    raise ValueError("Could not find appropriate value, consider pushing up starting offset")

utils.write_output(quineify(program), 17, a=1)

_e = time.time()
utils.print_time_diff(_s, _e, 17)