filename = "input.txt"

def mult(x, y): return x * y
def summ(x, y): return x + y

monkeys = []
operation = []
conditions = []

if_true = []
if_false = []

with open(filename) as file:
    index = -1
    for line in file:
        row = line.rstrip()
        if len(row) == 0: continue
        if row[0] == "M":
            print("Povecavam indeks")
            index += 1
        else:
            if row[2] == 'S':
                numbers = row.split(" ")[4:]
                arr = []
                for num in numbers:
                    if num.isnumeric():
                        arr.append(int(num))
                    else:
                        arr.append(int(num[:-1]))
                monkeys.append(arr)
            elif row[2] == 'O':
                operation.append(row.split(" ")[6] + "_" + row.split(" ")[7])
            elif row[2] == 'T':
                conditions.append(int(row.split(" ")[5]))
            else:
                con = row.split(" ")[5]
                num = row.split(" ")[9]
                if con == "true:":
                    if_true.append(int(num))
                else:
                    if_false.append(int(num))

    print("Za kraj")
    print(monkeys)
    print(operation)
    print(conditions)
    print(if_true)
    print(if_false)
    how_many_inspect = [0 for _ in range(len(monkeys))]
    for j in range(10000):
        print("RUNDA", j)
        print()
        for i in range(len(monkeys)):
            op = summ
            if operation[i].split("_")[0] == '*':
                op = mult
            for item in monkeys[i]:
                how_many_inspect[i] += 1
                sec_oper = item
                if operation[i].split("_")[1] != 'old':
                    sec_oper = int(operation[i].split("_")[1])
                curr_worry_lvl = op(item, sec_oper)
                if curr_worry_lvl % conditions[i] == 0:
                    monkeys[if_true[i]].append(curr_worry_lvl)
                else:
                    monkeys[if_false[i]].append(curr_worry_lvl)
            monkeys[i] = []


    first, second = sorted(how_many_inspect, reverse=True)[:2]
    print("FINAL SOLUTION:", first*second)
        


