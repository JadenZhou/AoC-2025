# with open("./sample.in") as fin:
with open("./input.in") as fin:
    lines = [line.strip() for line in fin.read().strip().splitlines()]

pos = 50    # starting position
count = 0   # number of zeros 

for instr in lines:

    direction = instr[0]
    val = int(instr[1:])
    
    if direction == "L":
        k0 = pos % 100
    elif direction == "R":
        k0 = (100 - pos) % 100

    if k0 == 0:
        k0 = 100

    if val >= k0:
        count += 1 + ((val - k0) // 100)

    if direction == "L":
        pos = (pos - val) % 100
    elif direction == "R":
        pos = (pos + val) % 100

print(count)
