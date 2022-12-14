filename = "input.txt"
vertiacal_walls = dict()
horizontal_walls = dict()
sand_occupied = []
max_y = 0
min_x = 1000
max_x = 0

cave = [['.' for _ in range(1000)] for _ in range(1000)]

def draw(draw_sand = False):
    global vertiacal_walls, horizontal_walls, sand_occupied
    for i in range(max_y+2):
        for j in range(min_x-1, max_x+1):
            print(cave[j][i], end="")
        print()


def simulate_fall():
    global cave, max_y
    falling = True
    coords_start = [500, 0]
    #print("Ulazim")
    while falling:
        falling = False
        if coords_start[1] == max_y+1: continue
        if cave[coords_start[0]][coords_start[1]+1] not in ['#', 'o']:
            coords_start[1] += 1
            falling = True
        elif cave[coords_start[0]-1][coords_start[1]+1] not in ['#', 'o']:
            coords_start[0] -= 1
            coords_start[1] += 1
            falling = True
        elif cave[coords_start[0]+1][coords_start[1]+1] not in ['#', 'o']:
            coords_start[0] += 1
            coords_start[1] += 1
            falling = True
    cave[coords_start[0]][coords_start[1]] = 'o'
    if coords_start == [500, 0]:
        return False
    #print("Evo stao je")
    #print("sand occupied:", sand_occupied)
    return True

with open(filename) as file:

    for line in file:
        straight_lines = line.rstrip().split(" -> ")
        for i in range(len(straight_lines) - 1):
            x1, y1 = [int(i) for i in straight_lines[i].split(",")]
            x2, y2 = [int(i) for i in straight_lines[i+1].split(",")]
            min_x = min(min(x1, x2), min_x)
            max_y = max(max(y1, y2), max_y)
            max_x = max(max(x1, x2), max_x)
            if x1 == x2:
                m_y, ma_y = [y1, y2] if y1 <= y2 else [y2, y1]
                for i in range(m_y, ma_y+1):
                    cave[x1][i] = "#"
            elif y1 == y2:
                m_x, ma_x = [x1, x2] if x1 <= x2 else [x2, x1]
                for i in range(m_x, ma_x+1):
                    cave[i][y1] = "#"
            else:
                raise Exception("Imamo kosu liniju i ne znam sta da radim u ovom slucaju")
    

    print("Y of lowest lvl:", max_y)
    print("X of lowest lvl:", min_x)
    print("X of highest lvl:", max_x)
    #draw()
    sand_stoped = True
    total = 0
    while sand_stoped:
        total += 1
        #print(total)
        sand_stoped = simulate_fall()
    print("Total of", total, "units of sand comes to rest.")
