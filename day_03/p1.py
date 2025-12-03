#with open("./sample.in") as fin:                                                          
with open("./input.in") as fin:                                                             
    banks = [bank.strip() for bank in fin.read().strip().splitlines()]

sum = 0

for bank in banks:

    b1 = bank[0]
    max_i = 0
    for i, battery in enumerate(bank[1:-1], start=1):
        if int(battery) > int(b1):
            b1 = battery
            max_i = i

    b2 = bank[max_i + 1]
    for battery in bank[max_i + 1:]:

        if int(battery) > int(b2):
            b2 = battery

    joltage = int(b1 + b2)
    sum += joltage

print(sum)
