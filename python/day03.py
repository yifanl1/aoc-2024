import utils
import re

inp = utils.get_input(3)
sample_inp = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
# inp = sample_inp

mul = lambda v: int(v[1]) * int(v[2])
mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

ans = sum(map(mul, re.finditer(mul_pattern, inp)))
utils.write_output(ans, day=3, w=True, append=False)

range_pattern = re.compile(r'(?:do\(\)|^)(.*?)(?:(don\'t\(\))|$)', re.DOTALL)
ranges = re.finditer(range_pattern, inp)
ans2 = sum(sum(map(mul, re.finditer(mul_pattern, r[1]))) for r in ranges)
utils.write_output(ans2, day=3, w=True, append=True)
