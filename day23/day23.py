filename = "input.txt"

def find_grid(arr):
    left_corner_x = min([x[0] for x in arr])
    left_corner_y = min([x[1] for x in arr])
    right_corner_x = max([x[0] for x in arr])
    right_corner_y = max([x[1] for x in arr])
    return [left_corner_x, left_corner_y], right_corner_y - left_corner_y + 1, right_corner_x-left_corner_x + 1

def is_elv(i, j, a):
    for elv in a:
        if elv[0] == i and elv[1]== j: return True
    return False

def print_grid(start, w, h, arr):
    for i in range(h):
        for j in range(w):
            if is_elv(i+start[0], j+start[1], arr):
                print("#", end="")
            else: print(".", end="")
        print()

def count_elves(w, h, arr):
    return w*h - len(arr)

def elves_around(elv, arr):
    for e in arr:
        if e == elv: continue
        if abs(elv[0] - e[0]) <= 1 and abs(elv[1]-e[1]) <= 1: return True
    return False

def get_positions(arr, idx):
    global check_sides
    arr_ret = []
    start_idx = idx
    for elv in arr:
        if not elves_around(elv, arr):
            arr_ret.append(False)
            continue
        idx = start_idx
        founded = False
        for _ in range(4):
            there_is_elve = False
            for new_check in check_sides[idx]:
                if [elv[0] + new_check[0], elv[1] + new_check[1]] in arr:
                    there_is_elve = True
                    break
            if not there_is_elve:
                arr_ret.append([elv[0] + check_sides[idx][1][0], elv[1] + check_sides[idx][1][1]])
                founded = True
                break
            idx = (idx + 1) % 4
        if not founded:
            arr_ret.append(False)
    return arr_ret

def check_possible(arr):
    ret_arr = arr[:]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                ret_arr[i] = False
                ret_arr[j] = False
    return ret_arr


check_sides = [((-1, -1), (-1, 0), (-1, 1)), ((1, -1), (1, 0), (1, 1)), ((-1, -1), (0, -1), (1, -1)), ((-1, 1), (0, 1), (1, 1))]

elves = []
num_of_row = 0
with open(filename) as file:

    for line in file:
        row = line.rstrip()
        for i, item in enumerate(row):
            if item == "#":
                elves.append([num_of_row, i])
        num_of_row += 1
print(elves)

grid_start, width, height = find_grid(elves)

#print_grid(grid_start, width, height, elves)
current_check = 0
for i in range(1000000):
    print(f'== End of Round {i+1} ==')
    possible_positions = get_positions(elves, current_check)
    new_positions = check_possible(possible_positions)
    new_elves = []
    if all(False == x for x in new_positions):
        print("zadnja runda")
        exit()
    for j in range(len(new_positions)):
        if new_positions[j]:
            new_elves.append(new_positions[j])
        else: new_elves.append(elves[j])
    elves = new_elves
    current_check = (current_check + 1) % 4
    #grid_start, width, height = find_grid(elves)
    #print_grid(grid_start, width, height, elves)
grid_start, width, height = find_grid(elves)
print("Part 1:", count_elves(width,height, elves))
