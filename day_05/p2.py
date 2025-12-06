#with open("./sample.in") as fin:                                                               
with open("./input.in") as fin:            
    fin1, fin2 = fin.read().strip().split("\n\n")
    ranges = [tuple(map(int, row.split("-"))) for row in fin1.splitlines()]

ranges.sort()

merged = []
cur_start, cur_end = ranges[0]
for s, e in ranges[1:]:
    if s <= cur_end + 1:
        cur_end = max(cur_end, e)
    else:
        merged.append((cur_start, cur_end))
        cur_start, cur_end = s, e

merged.append((cur_start, cur_end))

fresh = sum(e - s + 1 for s, e in merged)
print(fresh)
