def game(op, me):
    if (op == 'A' and me == 'Y') or (op == 'B' and me == 'Z') or (op == 'C' and me == 'X'):
        return 6
    if (op == 'A' and me == 'X') or (op == 'B' and me == 'Y') or (op == 'C' and me == 'Z'):
        return 3
    return 0

filename = "input.txt"
with open(filename) as file:
    num_of_points = dict()
    num_of_points['X'] = 1
    num_of_points['Y'] = 2
    num_of_points['Z'] = 3
    total = 0
    for line in file:
        points_in_round = 0
        row = line.rstrip().split(" ")
        opponent = row[0]
        me = row[1]
        points_in_round += game(opponent, me)
        points_in_round += num_of_points[me]
        total += points_in_round
print(total)

print("PART 2:")

def what_play(op, me):
    if me == 'X':
        if op == 'A':
            return 3
        elif op == 'B':
            return 1
        return 2
    elif me == 'Y':
        if op == 'A':
            return 1
        elif op == 'B':
            return 2
        return 3
    if op == 'A':
        return 2
    elif op == 'B':
        return 3
    return 1
filename = "input.txt"
with open(filename) as file:
    num_of_points = dict()
    num_of_points['X'] = 0
    num_of_points['Y'] = 3
    num_of_points['Z'] = 6
    total = 0
    for line in file:
        points_in_round = 0
        row = line.rstrip().split(" ")
        opponent = row[0]
        me = row[1]
        points_in_round += what_play(opponent, me)
        points_in_round += num_of_points[me]
        total += points_in_round
print(total)
