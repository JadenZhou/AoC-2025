#with open("./sample.in") as fin:                                                                
with open("./input.in") as fin:                                                                  
    lines = fin.read().split("\n")[:-1]
    nums = lines[:-1]
    ops = lines[-1:][0]

def read_num(i):
    num = ""
    for line in nums:
        num += line[i] if line[i] != " " else "" 
    return int(num)

n = len(nums[0])
sum = 0
op = ops[0]
ans = read_num(0)
for i in range(1, n):
    if i + 1 < len(ops) and ops[i+1] != " ":
        sum += ans
        op = ops[i+1]
        ans = 0 if op == "+" else 1
        continue
    
    if op == "+":
        ans += read_num(i)
    else:
        ans *= read_num(i)
sum += ans
print(sum)
