rules = {}
pages = []

if True:
    r, p = """1|2
1|3
2|3
2|4
3|4
4|1

1,2,3
2,3,4
3,4,1""".split("\n\n")
    for line in r.split('\n'):
        num, order = list(map(int,line.split('|')))

        if num not in rules:
            rules[num] = []

        rules[num].append(order)

    for line in p.split('\n'):
        pages.append(list(map(int,line.split(','))))

nums = list(set(list(rules.keys())))
n = len(nums)

for i in range(n):
    for j in range(n-i-1):
        num_1 = nums[j]
        num_2 = nums[j+1]

        if num_2 in list(rules.keys()):
            if num_1 in rules[num_2]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

corrects = []

for page in pages:
    correct = True
    init = -1
    for i in range(len(page)):
        num = page[i]

        current = nums.index(num)

        if current > init:
            init = current
        else:
            correct = False
            break
    if correct:
        corrects.append(page)

sum = 0

for c in corrects:
    i = int(len(c)/2)
    sum += c[i]

print(sum)