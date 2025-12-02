# with open("./sample.in") as fin:                                    
with open("./input.in") as fin:                                       
    ranges = [tuple(map(int, r.strip().split("-"))) for r in fin.read().strip().split(",")]

sum = 0
for lb, rb in ranges:
    for i in range(lb, rb + 1):
        if len(str(i)) % 2 == 1:
            continue

        mid = len(str(i)) // 2

        l = int(str(i)[:mid])
        r = int(str(i)[mid:])
        
        if l == r:
            sum += i

print(sum)
