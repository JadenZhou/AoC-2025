#with open("./sample.in") as fin:                                                          
with open("./input.in") as fin:                                                             
    banks = [bank.strip() for bank in fin.read().strip().splitlines()]

sum = 0
TURN_ON = 12

for bank in banks:

    num = ""
    prev_i = -1
    for i in range(TURN_ON):
        next_i = prev_i + 1
        b = bank[next_i]
        
        for j, battery in enumerate(bank[next_i+1:i-TURN_ON+1 if i < 11 else None], start=next_i+1):
            if int(battery) > int(b):
                b = battery
                next_i = j

        num += b
        prev_i = next_i

    joltage = int(num)
    sum += joltage

print(sum)
