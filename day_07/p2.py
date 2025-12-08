#with open("./sample.in") as fin:                                                                 
with open("./input.in") as fin:                                                                   
    lines = fin.read().strip().split("\n")                                                       

beams = [0 if c == "." else 1 for c in lines[0]]

for line in lines[2::2]:
    next = [0] * len(beams)
    for i, c in enumerate(line):
        if c == "^":
            next[i] = 0
            if i != 0:
                next[i-1] += beams[i]
            if i != len(line) - 1:
                next[i+1] += beams[i]
        else:
            next[i] += beams[i]

    beams = next

print(sum(beams))
