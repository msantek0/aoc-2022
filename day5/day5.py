stacks = [[] for _ in range(10)]
commands = []
filename = "input.txt"
arr = []
with open(filename) as file:
    counter = 0
    for line in file:
        row = line.rstrip()
        if len(row) > 0 and row[0] == 'm':
            commands.append(row)
            continue
        row = row.split(" ")
        cnt = 0
        help_arr = []
        for i, crane in enumerate(row):
            if crane == '':
                cnt+=1
            if cnt == 4:
                help_arr.append('')
                cnt = 0
            if crane != '':
                help_arr.append(crane)
        arr.append(help_arr)
    arr = arr[::-1]

    for line in arr:
        if len(line) > 0 and line[0] != '1':
            for i, crane in enumerate(line):
                if crane != '':
                    stacks[i].append(crane)
                
        
        
    for command in commands:
        cmd = command.split(" ")
        for i in range(int(cmd[1])):
            stacks[int(cmd[5])-1].append(stacks[int(cmd[3])-1][-1])
            stacks[int(cmd[3])-1].pop()
    print(stacks)

    print()
    print()
    final = []
    for i in stacks:
        if len(i) > 0:
            final.append(i[-1])
    print(final)



stacks = [[] for _ in range(10)]
commands = []
filename = "input.txt"
arr = []
with open(filename) as file:
    counter = 0
    for line in file:
        row = line.rstrip()
        if len(row) > 0 and row[0] == 'm':
            commands.append(row)
            continue
        row = row.split(" ")
        cnt = 0
        help_arr = []
        for i, crane in enumerate(row):
            if crane == '':
                cnt+=1
            if cnt == 4:
                help_arr.append('')
                cnt = 0
            if crane != '':
                help_arr.append(crane)
        arr.append(help_arr)
    arr = arr[::-1]

    for line in arr:
        if len(line) > 0 and line[0] != '1':
            for i, crane in enumerate(line):
                if crane != '':
                    stacks[i].append(crane)
                
        
        
    for command in commands:
        cmd = command.split(" ")
        for i in range(int(cmd[1])):
            stacks[int(cmd[5])-1].append(stacks[int(cmd[3])-1][(int(cmd[1])-i)*(-1)])
        for i in range(int(cmd[1])):
            stacks[int(cmd[3])-1].pop()
        

    print()
    print()
    final = []
    for i in stacks:
        if len(i) > 0:
            final.append(i[-1])
    print(final)


        