# with open("./sample.in") as fin:                                    
with open("./input.in") as fin:                                       
    ranges = [tuple(map(int, r.strip().split("-"))) for r in fin.read().strip().split(",")]

sum = 0
for lb, rb in ranges:
    for i in range(lb, rb + 1):

        num_len = len(str(i))
        mid = num_len // 2

        is_invalid = False
        for seq_len in range(1, mid + 1):

            seq = str(i)[0:seq_len]
            
            j = seq_len
            while j + seq_len <= num_len and not is_invalid:
                next_seq = str(i)[j:j+seq_len]
                
                if next_seq != seq:
                    break

                if j + seq_len == num_len:
                    is_invalid = True

                j += seq_len

        if is_invalid:
            sum += i 

print(sum)
