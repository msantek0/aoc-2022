filename = "input.txt"
with open(filename) as file:
    counter = 0
    for line in file:
        row = line.rsplit()[0]
        first, second = row.split(",")
        first_l, first_h = [int(i) for i in first.split("-")]
        second_l, second_h = [int(i) for i in second.split("-")]
        if first_l <= second_l and second_h <= first_h: counter += 1
        elif second_l <= first_l and first_h <= second_h: counter += 1

print(counter)


filename = "input.txt"
with open(filename) as file:
    counter = 0
    for line in file:
        row = line.rsplit()[0]
        first, second = row.split(",")
        first_l, first_h = [int(i) for i in first.split("-")]
        second_l, second_h = [int(i) for i in second.split("-")]
        if first_l <= second_l and second_l <= first_h: counter += 1
        elif second_l <= first_l and first_l <= second_h: counter += 1

print(counter)

