total_of_folder = dict()
folders_in_folder = dict()


def printaj(k, v, dubina):
    global folders_in_folder
    razmak = ""
    for _ in range(dubina):
        razmak += " "
    print(razmak, "-", k)
    razmak += " "
    for folder in v.split("-"):
        if folder in folders_in_folder:
            printaj(folder, folders_in_folder[folder], dubina+1)
        else:
            print(razmak, "-", folder)


filename = "input.txt"
with open(filename) as file:

    current_path = ""
    current_folder = ""
    for line in file:
        row = line.rstrip().split(" ")
        #print("current_path", current_path)
        #print("current_folder", current_folder)
        #print("naredba", row)
        if row[0] == '$':
            if row[1] == 'cd':
                if row[2] != '..':
                    current_path += '-'
                    current_path += row[2]
                    current_folder = row[2]
                else:
                    tmp = current_path.split("-")[:-1]
                    current_folder = current_path.split("-")[-2]
                    current_path = "-".join(tmp)
            elif row[1] == 'ls':
                continue
            else:
                print("DOSLO JE DO NEKE POGRESKE JER NIKAD NE BI TREBO UC TU")
                exit(1)
        elif row[0] == 'dir':
            if current_folder in folders_in_folder:
                folders_in_folder[current_folder] += '-'
                folders_in_folder[current_folder] += row[1]
            else:
                folders_in_folder[current_folder] = row[1]
        else:
            if current_folder in total_of_folder:
                total_of_folder[current_folder] += int(row[0])
            else:
                total_of_folder[current_folder] = int(row[0])

printaj("/", folders_in_folder["/"], 0)
