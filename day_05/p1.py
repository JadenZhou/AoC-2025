#with open("./sample.in") as fin:                                                               
with open("./input.in") as fin:            
    fin1, fin2 = fin.read().strip().split("\n\n")
    ranges = [tuple(map(int, row.split("-"))) for row in fin1.splitlines()]
    ingredients = [int(row.strip()) for row in fin2.splitlines()]

fresh = 0

for i in ingredients:
    for s, e in ranges:
        if i in range(s, e+1):
            fresh += 1
            break

print(fresh)
