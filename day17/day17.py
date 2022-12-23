from collections import deque

def print_cave(cave):
    for i in range(len(cave)):
        for j in range(7):
            print(cave[i][j], end="")
        print()

def check_next_layer(k, current_rock, cave):
    if k >= len(cave): return False
    lvl_of_rock = 0
    for j in range(k, -1, -1):
        if lvl_of_rock >= len(current_rock): return True
        layer = cave[j]
        if "#" in layer[current_rock[lvl_of_rock][0]:current_rock[lvl_of_rock][0]+current_rock[lvl_of_rock][1]]:
            return False
        lvl_of_rock +=1
    return True

filename = "input.txt"

movements = ""
with open(filename) as file:
    for line in file:
        movements = line.rstrip()

len_of_movements = len(movements)
print(len_of_movements)

def copy_rocks(rock):
    v = []
    for i in rock:
        tmp = [0, 0]
        tmp[0] = i[0]
        tmp[1] = i[1]
        v.append(tmp)
    return v

def solve(length):
    global rocks, idx_movement, len_of_movements, cave
    for i in range(length):
        current_rock = copy_rocks(rocks[i % 5][1:])
        #print(current_rock)
        most_left, most_right = rocks[i % 5][0]
        pocetak = idx_movement
        for j in range(4):
                
            movement = movements[idx_movement % len_of_movements]
            idx_movement += 1
            if movement == '>' and most_right < 7:
                most_right += 1
                most_left += 1
                for k in range(len(current_rock)):
                    current_rock[k][0] += 1
            elif movement == '<' and most_left > 0:
                most_left -= 1
                most_right -= 1
                for k in range(len(current_rock)):
                    current_rock[k][0] -= 1

        #print(current_rock)
        #print(most_left)
        #print(most_right)
        #print("Trenutno na indexu", idx_movement)
        if len(cave) == 0:
            layer = []
            for k in range(7):
                if k < most_left or k > most_right - 1: layer.append('.')
                else: layer.append('#')
            cave.append(layer)
            print(cave)
        else:
            falling = True
            k = -1
            while falling:
                k += 1
                falling = False
                if check_next_layer(k, current_rock, cave):
                    #print("Nisam smio uc tu")
                    falling = True
                    movement = movements[idx_movement % len_of_movements]
                    idx_movement += 1
                    if movement == '>' and most_right < 7:
                        most_right += 1
                        most_left += 1
                        for g in range(len(current_rock)):
                            current_rock[g][0] += 1
                        if not check_next_layer(k , current_rock, cave):
                            most_right -= 1
                            most_left -= 1
                            for g in range(len(current_rock)):
                                current_rock[g][0] -= 1
                    elif movement == '<' and most_left > 0:
                        most_left -= 1
                        most_right -= 1
                        for g in range(len(current_rock)):
                            current_rock[g][0] -= 1
                        if not check_next_layer(k , current_rock, cave):
                            most_right += 1
                            most_left += 1
                            for g in range(len(current_rock)):
                                current_rock[g][0] += 1
            on_witch_lvl = k-1
            lvl_of_rock = 0
            if on_witch_lvl > -1:
                for j in range(on_witch_lvl, -1, -1):
                    if lvl_of_rock >= len(current_rock): break
                    layer = cave[j]
                    for k in range(len(layer)):
                        if k >= current_rock[lvl_of_rock][0] and k < current_rock[lvl_of_rock][0]+current_rock[lvl_of_rock][1]: layer[k] = '#'
                    lvl_of_rock += 1
            if lvl_of_rock < len(current_rock):
                for i in range(lvl_of_rock, len(current_rock)):
                    layer = []
                    for k in range(7):
                        if k >= current_rock[i][0] and k < current_rock[i][0]+current_rock[i][1]: layer.append('#')
                        else: layer.append('.')
                    
                    cave.appendleft(layer)
                #if lvl_of_rock == 0 and cnt % 5 == 0 and all(cave[0][j] == ['.', '.', '#', '#', '#', '#', '.'][j] for j in range(7)):
                #        print(cnt)
    

# First array in each rock represents its most left coord, and most right coored
rocks = [[(2, 6), (2, 4)], 
         [(2, 5), (3, 1), (2, 3), (3, 1)], 
         [(2, 5), (2, 3), (4, 1), (4, 1)],
         [(2, 3), (2, 1), (2, 1), (2, 1), (2, 1)],
         [(2, 4), (2, 2), (2, 2)]]

top_rock = 0

idx_movement = 0
pocetak = 0
first = 0 
second = len_of_movements*5*10
cnt = 0
cave = deque()
solve(2022)
print("Part 1 height:", len(cave))


# NOT WORKING !!!
# length of cycle is 50455
# so the final solution is 19819641 * 50455 + 13345
#cave = deque()
#solve(50455)
#cycle_len = len(cave)
#cave = deque()
#solve(13345)
#print("Part 2:", 19819641 * cycle_len + len(cave))
