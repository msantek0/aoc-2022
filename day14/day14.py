filename = "input.txt"
vertiacal_walls = dict()
horizontal_walls = dict()
sand_occupied = []
max_y = 0
min_x = 1000
max_x = 0

def draw(draw_sand = False):
    global vertiacal_walls, horizontal_walls, sand_occupied
    for i in range(max_y+2):
        for j in range(min_x-1, max_x+1):
            if i == 0 and j == 500: 
                print('+', end="")
                continue
            if in_vertical(j, i) or in_horizontal(j, i): print("#", end="")
            else: 
                if draw_sand and [j, i] in sand_occupied:
                    print("o", end="")
                else: print(".", end="")
        print()

def in_vertical(x, y):
    global vertiacal_walls
    #print("Tu stalno ulazim", x, y)
    if x in vertiacal_walls:
        for cords in vertiacal_walls[x]:
            if y >= cords[0] and y <= cords[1]:
                return True
    return False

def in_horizontal(x, y):
    global horizontal_walls
    if y in horizontal_walls:
        for cords in horizontal_walls[y]:
            if x >= cords[0] and x <= cords[1]:
                return True
    return False

def is_free(x, y):
    global sand_occupied
    if in_vertical(x,y): return False
    if in_horizontal(x, y): return False
    if [x, y] in sand_occupied: return False
    return True

def simulate_fall():
    global sand_occupied, max_y
    falling = True
    coords_start = [500, 0]
    #print("Ulazim")
    while falling:
        falling = False
        if is_free(coords_start[0], coords_start[1]+1):
            coords_start[1] += 1
            falling = True
            if coords_start[1] > max_y:
                print("Evo doslo je", coords_start[1])
                return False
        elif is_free(coords_start[0]-1, coords_start[1]+1):
            coords_start[0] -= 1
            coords_start[1] += 1
            falling = True
        elif is_free(coords_start[0]+1, coords_start[1]+1):
            coords_start[0] += 1
            coords_start[1] += 1
            falling = True
        
    sand_occupied.append(coords_start)
    #print("Evo stao je")
    #print("sand occupied:", sand_occupied)
    return True

with open(filename) as file:

    for line in file:
        straight_lines = line.rstrip().split(" -> ")
        for i in range(len(straight_lines) - 1):
            x1, y1 = [int(i) for i in straight_lines[i].split(",")]
            x2, y2 = [int(i) for i in straight_lines[i+1].split(",")]
            if y1 > max_y:
                max_y = y1
            if y2 > max_y:
                max_y = y2
            if x1 > max_x:
                max_x = x1
            if x2 > max_x:
                max_x = x2
            if x1 < min_x:
                min_x = x1
            if x2 < min_x:
                min_x = x2
            if x1 == x2:
                if x1 in vertiacal_walls:
                    tmp = [y1, y2] if y1 <= y2 else [y2, y1]
                    if tmp not in vertiacal_walls[x1]:
                        vertiacal_walls[x1].append(tmp)
                else:
                    vertiacal_walls[x1] = [[y1, y2]] if y1 <= y2 else [[y2, y1]]
            elif y1 == y2:
                if y1 in horizontal_walls:
                    tmp = [x1, x2] if x1 <= x2 else [x2, x1]
                    if tmp not in horizontal_walls[y1]:
                        horizontal_walls[y1].append(tmp)
                else:
                    horizontal_walls[y1] = [[x1, x2]] if x1 <= x2 else [[x2, x1]]
            else:
                raise Exception("Imamo kosu liniju i ne znam sta da radim u ovom slucaju")
    
    print(vertiacal_walls)
    print(horizontal_walls)
    print("Y of lowest lvl:", max_y)
    print("X of lowest lvl:", min_x)
    print("X of highest lvl:", max_x)
    draw()
    sand_stoped = True
    total = 0
    while sand_stoped:
        total += 1
        sand_stoped = simulate_fall()
    print("Total of", total-1, "units of sand comes to rest.")
    print(sand_occupied)
    draw(True)