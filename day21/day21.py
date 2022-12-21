
def rijesi(monkey, start):
    if isinstance(monkey[start], list):
        left = rijesi(monkey, monkey[start][0])
        right = rijesi(monkey, monkey[start][2])
        operator = monkey[start][1]
        if operator == "+":
            return left + right
        if operator == "-":
            return left - right
        if operator == "/":
            return left // right
        if operator == "*":
            return left * right
    else:
        return monkey[start]

filename = "input.txt"
monkeys = dict()
with open(filename) as file:
    for line in file:
        row = line.rstrip().split(" ")
        if row[1].isnumeric():
            monkeys[row[0][:-1]] = int(row[1])
        else:
            monkeys[row[0][:-1]] = row[1:]



print("Part 1: ", rijesi(monkeys, "root"))

value_humn = 0
increment_value = 1
previous_difference = None

#Binary search for answer

# we know that humn is always on a left side
right = rijesi(monkeys, monkeys['root'][2]) 

while True:
    monkeys['humn'] = value_humn    
    left = rijesi(monkeys, monkeys['root'][0])
    if left == right:
      print("Part 2: ", value_humn)
      break
    difference = left - right
    if  ( difference < 0 ) == previous_difference:
      increment_value *= 2
    else:
      increment_value = -1 if difference < 0 else 1

    previous_difference = difference < 0  
    value_humn += increment_value