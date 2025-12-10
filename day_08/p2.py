import math

#with open("./sample.in") as fin:                                                                  
with open("./input.in") as fin:                                                                    
    coords = [tuple(map(int, line.split(","))) for line in fin.read().strip().split("\n")]                                                        

def euclidean(p1, p2):
    sum = 0
    for x1, x2 in zip(p1, p2):
        sum += (x1 - x2) ** 2
    return math.sqrt(sum)

boxes = len(coords)
distances = [] 
for i in range(boxes):
    for j in range(i + 1, boxes):
        distances += [(euclidean(coords[i], coords[j]), (i, j))]

distances.sort()

clusters = [[i] for i in range(len(coords))]

prod = None

while len(clusters) > 1:
    closest, (c1, c2) = distances.pop(0)

    c1_i = None
    c2_i = None
    for i, cluster in enumerate(clusters):
        if c1 in cluster:
            c1_i = i
        if c2 in cluster:
            c2_i = i

        if c1_i is not None and c2_i is not None:
            break
    if c1_i == c2_i:
        continue
    
    if len(clusters) == 2:
        prod = coords[c1][0] * coords[c2][0]
    i_small = min(c1_i, c2_i)
    i_big = max(c1_i, c2_i)
    clusters[i_small] += clusters.pop(i_big)

print(prod)
