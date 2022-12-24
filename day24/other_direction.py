import copy
filename = "input.txt"

start_x = 25 if filename == "input.txt" else 4
start_y = 119 if start_x == 25 else 5
start_wind = 257 if start_x == 25 else 18 #replace with your output of part 1
class Wind():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, h, w):
        new_x = self.x + self.direction[0]
        new_y = self.y + self.direction[1]
        if new_x < 0:
            new_x = h-1
        elif new_x == h:
            new_x = 0
        if new_y < 0:
            new_y = w-1
        elif new_y == w:
            new_y = 0
        self.x = new_x
        self.y = new_y 

    def __str__(self) -> str:
        return f'({self.x}, {self.y}) and direction: {self.direction}'

class Expedition():
    def __init__(self, x, y, steps, parent):
        self.x = x
        self.y = y
        self.steps = steps
        self.parent = parent

def there_is_no_wind(winds, x, y):
    for wind in winds:
        if wind.x == x and wind.y == y: return False
    return True


def find_new_positions(position, queue):
    global winds, width, height, possible_movements, visited
    for dx, dy in possible_movements:
        if position.x + dx == -1 and position.y + dy == 0:
            print("Naso sam rijesenje:", position.steps + 1 - start_wind)
            exit()
        if dx + position.x < -1 or position.x + dx >= height: continue
        if dy + position.y < 0 or dy + position.y >= width: continue
        if dy + position.y != 0 and dx + position.x < 0: continue
        if there_is_no_wind(winds[position.steps+1], position.x + dx, position.y + dy):
            if [position.x + dx, position.y + dy, position.steps + 1] not in visited:
                queue.append(Expedition(dx + position.x, dy + position.y, position.steps + 1, position))
                visited.append([position.x + dx, position.y + dy, position.steps + 1])

    if there_is_no_wind(winds[position.steps+1], position.x, position.y):
        if [position.x, position.y, position.steps + 1] not in visited:
            queue.append(Expedition(position.x, position.y, position.steps + 1, position))
            visited.append([position.x, position.y, position.steps + 1])
    

possible_movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
starting_winds = []
num_of_row = 0
width = -1
height = -1
all_steps = []
with open(filename) as file:
    for line in file:
        row = line.rstrip()
        if num_of_row == 0: 
            width = len(row) - 2
            num_of_row += 1
            continue
        for i, point in enumerate(row):
            if point not in [".", "#"]:
                if point == "<":
                    starting_winds.append(Wind(num_of_row-1, i-1, (0, -1)))
                elif point == ">":
                    starting_winds.append(Wind(num_of_row-1, i-1, (0, 1)))
                elif point == "v":
                    starting_winds.append(Wind(num_of_row-1, i-1, (1, 0)))
                elif point == "^":
                    starting_winds.append(Wind(num_of_row-1, i-1, (-1, 0)))
                else:
                    print("Doslo je do pogreške jer nemoguće da postoji jos neki drugi znak")
                    print("Znak:", point)
                    assert False
        num_of_row += 1
height = num_of_row - 2
print(width)
print(height)

winds = [copy.deepcopy(starting_winds)]
from time import time
start = time()
for i in range(1000):
    for wind in starting_winds:
        wind.move(height, width)
    winds.append(copy.deepcopy(starting_winds))

print("zavrsio za:", time()-start)

que = []
visited = []
que.append(Expedition(start_x, start_y, start_wind, None))
visited.append([start_x, start_y, start_wind])
while que:
    p = que.pop(0)

    find_new_positions(p, que)
    #print(len(visited))
    #print(len(que))