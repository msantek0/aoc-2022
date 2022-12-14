filename = "input.txt"

trenutni = [[0, 0] for i in range(10)]
glavni_put = [[trenutni[i][:]] for i in range(10)]
with open(filename) as file:
    for line in file:
        direction, num_of_steps = line.rstrip().split(" ")
        #print(direction, num_of_steps)
        for i in range(int(num_of_steps)):
            pomocni = [trenutni[i][:] for i in range(10)]

            if direction == 'U':
                pomocni[0][1] += 1
            elif direction == 'D':
                pomocni[0][1] -= 1
            elif direction == 'R':
                pomocni[0][0] += 1
            else:
                pomocni[0][0] -= 1
            glavni_put[0].append(pomocni[0])
            for i in range(1, 10):

                if abs(pomocni[i][0] - pomocni[i-1][0]) > 1:
                    
                    #mora se micat 
                    pomak_x = int((pomocni[i-1][0] - pomocni[i][0]) / 2)
                    if abs(pomocni[i-1][1] - pomocni[i][1]) > 1:
                        pomak_y = int((pomocni[i-1][1] - pomocni[i][1])/2)
                    else:
                        pomak_y = int(pomocni[i-1][1] - pomocni[i][1])
                    pomocni[i][0] += pomak_x
                    pomocni[i][1] += pomak_y
                    glavni_put[i].append(pomocni[i])
                elif abs(pomocni[i][1] - pomocni[i-1][1]) > 1:
                    pomak_y = int((pomocni[i-1][1] - pomocni[i][1]) / 2)
                    if abs(pomocni[i-1][0] - pomocni[i][0]) > 1:
                        pomak_x = int((pomocni[i-1][0] - pomocni[i][0])/2)
                    else:
                        pomak_x = int(pomocni[i-1][0] - pomocni[i][0])
                    pomocni[i][0] += pomak_x
                    pomocni[i][1] += pomak_y
                    glavni_put[i].append(pomocni[i])
                trenutni[i] = pomocni[i][:]
                trenutni[i-1] = pomocni[i-1][:]

    za_brojanje = []
    print(glavni_put)
    for i, glavni in enumerate(glavni_put):
        print(i,": ",  glavni)
    for dot in glavni_put[9]:
        if dot not in za_brojanje: za_brojanje.append(dot)
    print(za_brojanje)
    print("KONACNO RJESENJE", len(za_brojanje))   
