total_of_folder = dict()
folders_in_folder = dict()



filename = "input.txt"
with open(filename) as file:

    current_path = ""
    current_folder = ""
    for line in file:
        row = line.rstrip().split(" ")
        #print("current_path", current_path)
        ##print("current_folder", current_folder)
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
            if current_path in folders_in_folder:
                folders_in_folder[current_path] += '_'
                folders_in_folder[current_path] += current_path + "-" + row[1]
            else:
                folders_in_folder[current_path] = current_path + "-" + row[1]
        else:
            if current_path in total_of_folder:
                total_of_folder[current_path] += int(row[0])
            else:
                total_of_folder[current_path] = int(row[0])

print(total_of_folder)
print(folders_in_folder)
cnt =0
while len(folders_in_folder) > 0:
    cnt += 1
    print(cnt)
    za_brisanje = []
    for k, v in folders_in_folder.items():
        check = True
        #print()
        #print("SADA RADIM ZA ", k)
        
        #print("TRENUTNI folder", folders_in_folder)

        for folder in v.split("_"):
            if folder in folders_in_folder:
                print("PUCAM NA",folder)
                check = False
                break
        if check:
            for f in v.split("_"):
                #print("NEGOV f je", f)
                zbroji = 0
                if f in total_of_folder:
                    zbroji = total_of_folder[f]
                if k in total_of_folder:
                    total_of_folder[k] += zbroji
                else:
                    total_of_folder[k] = zbroji
            za_brisanje.append(k)
    if len(za_brisanje) == 0:
        print("SAD VEC NEMA NISTA")
        print(folders_in_folder)
    print(za_brisanje)
    for k in za_brisanje:
        folders_in_folder.pop(k, None)
        for key, v in folders_in_folder.items():
            new_v = ""
            for a in v.split("_"):
                if a == k:
                    if a in total_of_folder:
                        if key in total_of_folder:
                            total_of_folder[key] += total_of_folder[a]
                        else:
                            total_of_folder[key] = total_of_folder[a]
                    continue
                new_v += a
                new_v += "_"
            new_v = new_v[:-1]
            folders_in_folder[key] = new_v

print(total_of_folder)
print(folders_in_folder)





total = 0
for k, v in total_of_folder.items():
    if v <= 100000:
        total += v
print("Konacno rjesenje part 1 je:", total)


print("Ukupno zauzece memorije:", total_of_folder["-/"])
ukupno_slobodno = 70000000 - total_of_folder["-/"]
print("Ukupno slobdono mjesta:", ukupno_slobodno)
jos_potrebno = 30000000 - ukupno_slobodno
print("Jos potrebno mjesta za osloboditi je:", jos_potrebno)

all_aviable = dict()
for k, v in total_of_folder.items():
    if v >= jos_potrebno:
        all_aviable[k] = v

print(sorted(all_aviable.items(), key=lambda x: x[1])[0])
