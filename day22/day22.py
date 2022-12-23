filename = "input.txt"
map_of_the_board = []
num_of_row = 0
instructions_on = False
instructions = []
found = False
postion = []
max_length = -1
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end="")
        print()


with open(filename) as file:
    for line in file:
        if instructions_on:
            cnt = 0
            row = line.rstrip()
            while cnt < len(row):
                if row[cnt] in ["L", "R"]:
                    instructions.append(row[cnt])
                    cnt += 1
                    continue
                num_cnt = cnt
                while num_cnt < len(row) and row[num_cnt] not in ["L", "R"]: num_cnt += 1
                instructions.append(int(row[cnt:num_cnt]))
                cnt = num_cnt

        if len(line.rstrip()) == 0: instructions_on = True
        if not instructions_on:
            map_of_the_board.append([])
            if num_of_row == 0:
                max_length = len(line.rstrip())
            row = line.rstrip()
            for i in range(max_length):
                if len(row) <= i or row[i] not in [".", "#"]: map_of_the_board[num_of_row].append("0")
                else: 
                    if row[i] == "." and not found and num_of_row == 0:
                        found = True
                        postion.append(num_of_row)
                        postion.append(i)
                    map_of_the_board[num_of_row].append(row[i])
            num_of_row += 1

#print_board(map_of_the_board)
#print(instructions)
#print(postion)
#print(map_of_the_board[50][140])
horizontal_length = len(map_of_the_board[0])
vertical_length = len(map_of_the_board)

#print(map_of_the_board[89][49:60])
orientation = [(0, 1), (1, 0), (0, -1), (-1, 0)]
current_orentation = 0
for test, inst in enumerate(instructions):
    #print((postion[1], postion[0]), inst)
    #if test == 1116:
    #    print((postion[1], postion[0]), inst, orientation[current_orentation])
    if inst == "L":
        current_orentation = (current_orentation - 1) % len(orientation)
    elif inst == "R":
        current_orentation = (current_orentation + 1) % len(orientation)
    else:
        for i in range(inst):
            #if test == 1116:
            #    print(postion)
            if postion[0] + orientation[current_orentation][0] >= vertical_length or postion[0] + orientation[current_orentation][0] < 0 or map_of_the_board[postion[0] + orientation[current_orentation][0]][postion[1]] == "0":
                new_idx = postion[0] + orientation[current_orentation][0]
                if orientation[current_orentation][0] == 1:
                    new_idx -= 1
                    #print("Hej", new_idx, "dok je vertiacl", vertical_length)
                    while new_idx >= 0 and map_of_the_board[new_idx][postion[1]] != "0":
                        #print("Iz wilea", new_idx)
                        new_idx -= 1
                    if map_of_the_board[new_idx + 1][postion[1]] == "#": break
                    postion[0] = new_idx + 1
                    continue
                elif orientation[current_orentation][0] == -1:
                    new_idx += 1
                    while new_idx < vertical_length and map_of_the_board[new_idx][postion[1]] != "0": 
                        new_idx += 1
                    if map_of_the_board[new_idx - 1][postion[1]] == "#": break
                    postion[0] = new_idx - 1
                    continue
                else:
                    print("DOSOLO JE DO NEKE GRDE GRESKE 74")
                    exit()
            if postion[1] + orientation[current_orentation][1] >= horizontal_length or postion[1] + orientation[current_orentation][1] < 0 or map_of_the_board[postion[0]][postion[1] + orientation[current_orentation][1]] == "0":
                new_idx = postion[1] + orientation[current_orentation][1]
                if orientation[current_orentation][1] == 1:
                    new_idx -= 1

                    while new_idx >= 0 and map_of_the_board[postion[0]][new_idx] != "0": 
                        new_idx -= 1
                    if map_of_the_board[postion[0]][new_idx+1] == "#": break
                    postion[1] = new_idx + 1
                    continue
                elif orientation[current_orentation][1] == -1:
                    new_idx += 1
                    while new_idx < horizontal_length and map_of_the_board[postion[0]][new_idx] != "0": new_idx += 1
                    if map_of_the_board[postion[0]][new_idx-1] == "#": break
                    postion[1] = new_idx - 1
                    continue
                else:
                    print("DOSOLO JE DO NEKE GRDE GRESKE 89")
                    exit()
            if map_of_the_board[postion[0] + orientation[current_orentation][0]][postion[1] + orientation[current_orentation][1]] == "#": break
            
            postion[0] += orientation[current_orentation][0]
            postion[1] += orientation[current_orentation][1]
print("Part 1:", 1000 * (postion[0] + 1) + 4 * (postion[1] + 1) + current_orentation)
