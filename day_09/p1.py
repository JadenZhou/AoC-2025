#with open("./sample.in") as fin:                                                                                                                  
with open("./input.in") as fin:                                                                                                                    
    reds = [tuple(map(int, line.split(","))) for line in fin.read().strip().split("\n")]         

def area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    width = abs(x1 - x2) + 1
    length = abs(y1 - y2) + 1
    
    return length * width

max_area = 0

for c1 in reds:
    for c2 in reds:
        if c1 == c2: 
            continue

        if area(c1, c2) > max_area:
            max_area = area(c1, c2)

print(max_area)


