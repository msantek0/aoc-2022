
filename = "input.txt"
with open(filename) as file:
    counter = 0
    for line in file:
        row = line.rstrip()
        print(row)
        for i, letter in enumerate(row):
            tmp = set()
            for j in range(4):
                tmp.add(row[i+j])
            if len(tmp) > 3:
                print(i+4)
                break

filename = "input.txt"
with open(filename) as file:
    counter = 0
    for line in file:
        row = line.rstrip()
        print(row)
        for i, letter in enumerate(row):
            tmp = set()
            for j in range(14):
                tmp.add(row[i+j])
            if len(tmp) > 13:
                print(i+14)
                break
