#with open("./sample.in") as fin:                                                                
with open("./input.in") as fin:                                                                  
    lines = fin.read().strip().split("\n")
    nums = [[int(num.strip()) for num in line.split()] for line in lines[:-1]]
    ops = [op.strip() for op in lines[-1:][0].split()]

sum = 0
for i in range(len(nums[0])):
    ans = nums[0][i]
    op = ops[i]
    for j in range(1, len(lines) - 1):
        if op == "+":
            ans += nums[j][i]
        else:
            ans *= nums[j][i]
    sum += ans

print(sum)
