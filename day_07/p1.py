#with open("./sample.in") as fin:                                                                 
with open("./input.in") as fin:                                                                   
    lines = fin.read().strip().split("\n")                                                       

beams = [0 if c == "." else 1 for c in lines[0]]
split = 0

for line in lines[1:]:
    for i, c in enumerate(line):
        if c == "^":
            if beams[i] == 1:
                split += 1
            beams[i] = 0
            if i != 0:
                beams[i-1] = 1
            if i != len(line) - 1:
                beams[i+1] = 1

print(split)
