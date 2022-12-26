filename = "input.txt"

DIC = {'-': -1, '=': -2}
all_fives = [pow(5, i) for i in range(20)]

def to_decimal(row):
    global DIC, all_fives
    decimal = 0
    for i, s in enumerate(row):
        if s in DIC:
            decimal += DIC[s] * all_fives[i]
        else:
            decimal += int(s) * all_fives[i]
    return decimal

def to_SNAFU(number):
    res = ""
    while number:
        tmp=number%5
        if tmp == 3: tmp = "="
        if tmp == 4: tmp = "-"
        res +=  str(tmp)
        if number>2: number+=2
        number//=5
    return res[::-1]


total = 0
with open(filename) as file:

    for line in file:
        total += to_decimal(line.rstrip()[::-1])

#print(to_SNAFU(3))
print("Part 1:", to_SNAFU(total))