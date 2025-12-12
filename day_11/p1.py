with open("./sample.in") as fin:                                                                                                                   
#with open("./input.in") as fin:       
    lines = fin.read().strip().split("\n")
    adj_l = []
    for line in lines:
        v, adjs = line.split(":")
        adjs = adjs.strip().split(" ")
        adj_l += [(v, adjs)]

print(adj_l)
