with open("./sample.in") as fin:                                    
# with open("./input.in") as fin:                                       
    ranges = [tuple(map(int, r.strip().split("-"))) for r in fin.read().strip().split(",")]

print(ranges)
