# with open("./sample.in") as fin:
with open("./input.in") as fin:
    lines = [line.strip() for line in fin.read().strip().splitlines()]

pos = 50    # starting position
count = 0   # number of zeros 

for instr in lines:

    direction = instr[0]
    val = int(instr[1:])
    
    if direction == "L":
        pos = (pos - val) % 100
    elif direction == "R":
        pos = (pos + val) % 100
    else:
        raise ValueError(f"Unknown instruction: {instr}")

    if pos == 0:
        count += 1

print(count)
