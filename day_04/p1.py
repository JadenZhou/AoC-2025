#with open("./sample.in") as fin:                                                            
with open("./input.in") as fin:                                                              
    grid = [list(row.strip()) for row in fin.read().strip().splitlines()]                      

length = len(grid)
width = len(grid[0])

def access(y, x):
    
    nw = grid[y-1][x-1] if y != 0 and x != 0 else None
    n = grid[y-1][x] if y != 0 else None
    ne = grid[y-1][x+1] if y != 0 and x != width-1 else None
    w = grid[y][x-1] if x != 0 else None
    e = grid[y][x+1] if x != width-1 else None
    sw = grid[y+1][x-1] if y != length-1 and x != 0 else None
    s = grid[y+1][x] if y != length-1 else None
    se = grid[y+1][x+1] if y != length-1 and x != width-1 else None

    adj = [nw, n, ne, w, e, sw, s, se].count("@")
    
    return adj < 4


rolls = 0
for i in range(length):
    for j in range(width):
        if grid[i][j] == "@" and access(i, j):
            rolls += 1

print(rolls)
