filename = "input.txt"

trenutni_H = [0, 0]
trenutni_T = [0, 0]
T = [trenutni_T[:]]
H = [trenutni_H[:]]
print("NA pocetku", H)
with open(filename) as file:
    for line in file:
        direction, num_of_steps = line.rstrip().split(" ")
        #print(direction, num_of_steps)
        for i in range(int(num_of_steps)):
            pomH = trenutni_H[:]

            pomT = trenutni_T[:]

            if direction == 'U':
                pomH[1] += 1
            elif direction == 'D':
                pomH[1] -= 1
            elif direction == 'R':
                pomH[0] += 1
            else:
                pomH[0] -= 1
            H.append(pomH)
            if abs(pomT[0] - pomH[0]) > 1:
                #mora se micat 
                pomak_x = int((pomH[0] - pomT[0]) / 2)
                pomak_y = int(pomH[1] - pomT[1])
                pomT[0] += pomak_x
                pomT[1] += pomak_y
                T.append(pomT)
            elif abs(pomT[1] - pomH[1]) > 1:
                pomak_y = int((pomH[1] - pomT[1]) / 2)
                pomak_x = int(pomH[0] - pomT[0])
                pomT[0] += pomak_x
                pomT[1] += pomak_y
                T.append(pomT)
            trenutni_T = pomT[:]
            trenutni_H = pomH[:]
    print(H)
    print(T)
    za_brojanje = []
    for dot in T:
        if dot not in za_brojanje: za_brojanje.append(dot)

    print("KONACNO RJESENJE", len(za_brojanje))   
