import math
filename = "input.txt"
ROW_OF_INTEREST = 2000000 if filename == "input.txt" else 10
AREA_OF_INTEREST = 4000000 if filename == "input.txt" else 20

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)



def solve_for_row(y):
    global beacons, max_beacon, min_beacon, idx_of_beacons_in_row_of_interest, distance
    cnt_number_of_taken = 0
    for i in range(min_beacon, 999999999999999999999999):
        print("Ulazim za i:", i)
        if i in idx_of_beacons_in_row_of_interest: continue
        promjena = False
        for idx, sensor in enumerate(sensors):
            dist = manhattan_distance(sensor[0], sensor[1], i, y)
            if dist <= distance[idx]:
                promjena = True
                cnt_number_of_taken += 1
                break
        if i > max_beacon and not promjena:
            break
    for i in range(min_beacon-1,-999999999999999999999999, -1):
        print("Negativno: ulazim za i:", i)
        if i in idx_of_beacons_in_row_of_interest: continue
        promjena = False
        for idx, sensor in enumerate(sensors):
            dist = manhattan_distance(sensor[0], sensor[1], i, y)
            if dist <= distance[idx]:
                promjena = True
                cnt_number_of_taken += 1
                break
        if i < min_beacon and not promjena:
            break
    return cnt_number_of_taken

def check_spot(x, y):
    global sensors, distance
    for idx, sensor in enumerate(sensors):
        dist = manhattan_distance(sensor[0], sensor[1], x, y)
        if dist <= distance[idx]:
            return False
    return True

def check_edges(sensor, idx):
    global AREA_OF_INTEREST, distance
    print("Ulazim za senzor:", sensor)
    print("distance mu je:", distance[idx])
    j = 0
    for i in range(sensor[1]-distance[idx], sensor[1]+distance[idx] + 1):
        #print("Rjesavam i", i)
        j += 1
        if i > AREA_OF_INTEREST or i < 0: 
            continue
        if sensor[0] + j <= AREA_OF_INTEREST and sensor[0] + j > 0:
            if check_spot(sensor[0]+j, i):
                return sensor[0]+j, i
        if sensor[0] - j <= AREA_OF_INTEREST and sensor[0] - j > 0:
            if check_spot(sensor[0]-j, i):
                return sensor[0]-j, i

    return -1, -1

def part_two(): 
    global sensors
    for idx, sensor in enumerate(sensors):
        x, y = check_edges(sensor, idx)
        if x!= -1 and y!= -1:
            return x, y
    return -1, -1


sensors = []
beacons = []
distance = []
array_of_unav = []
all_sensors_of_beacon = dict()
idx_of_beacons_in_row_of_interest = []
max_beacon = -math.inf
min_beacon = math.inf
with open(filename) as file:

    for line in file:
        row = line.rstrip().split(" ")
        s_x = int(row[2][:-1].split("=")[1])
        s_y = int(row[3][:-1].split("=")[1])
        b_x = int(row[8][:-1].split("=")[1])
        b_y = int(row[9].split("=")[1])
        if (b_x, b_y) in all_sensors_of_beacon:
            all_sensors_of_beacon[(b_x, b_y)].append([s_x, s_y])
        else:
            all_sensors_of_beacon[(b_x, b_y)] = [[s_x, s_y]]
        sensors.append([s_x, s_y])
        beacons.append([b_x, b_y])
        distance.append(manhattan_distance(s_x, s_y, b_x, b_y))
        max_beacon = max(b_x, max_beacon)
        max_beacon = max(s_x, max_beacon)
        min_beacon = min(b_x, min_beacon)
        min_beacon = min(s_x, min_beacon)
        if ROW_OF_INTEREST == b_y:
            idx_of_beacons_in_row_of_interest.append(b_x)
print("Sensors:")
print(sensors)
print()
print("Beacons:")
print(beacons)
print("Max i Min beacon:", max_beacon, min_beacon)




# Prvi dio se malo duze vrti pa ga rade drzim zakomentiranog


#print("Ukupno slobodnog mjesta:", solve_for_row(ROW_OF_INTEREST))

print("Let's statr with part two")

x, y = part_two()
print("x:", x, "y:", y)

# Za drugi dio je ideja da se samo gledaju rubovi nasih senzora jer samo na rubu moze biti tocka
# zato jer je jedinstvena, i kad ne bi bila na rubu od nekog senzora onda bi bilo vise od 1 tocke


print("PART 2:", x*4000000 + y)