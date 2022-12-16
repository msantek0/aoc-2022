class Cell:
    def __init__(self, x, y, l, dist, prev) :
        self.x = x
        self.y = y
        self.letter = l
        self.dist = dist; #distance to start
    def __str__(self):
        return "("+ str(self.x) + "," + str(self.y) + ")" 

filename = "input.txt"
location_S = []
location_E = []
cnt_rows = 0
mapa = []
queue = []
visited = []
all_a_letters = []

def BFS():
    global mapa, location_S, location_E, queue, visited
    queue.append(Cell(location_S[0], location_S[1], "a", 0, None))
    dest = None
    p = queue.pop(0)
    visited.append([p.x, p.y])
    while p != None:

        #print("Ulazim za:", p.x, p.y, p.letter)
        if p.x == location_E[0] and p.y == location_E[1]:
            dest = p
            break
        # moving up
        visit(p.x-1, p.y, p)
        visit(p.x, p.y-1, p)     
        visit(p.x+1, p.y, p)      
        visit(p.x, p.y+1, p)
        #print("Ali status queae", len(queue))
        p = None
        if len(queue) > 0:
            p = queue.pop(0)

    
    if dest == None :
        print("there is no path.")
        return 1000000
    else :
        return p.dist
        

def visit(x, y, parent):
    global mapa, queue, visited
    if x < 0 or x >= len(mapa) or y < 0 or y >= len(mapa[0]) or mapa[x][y] == None :
        return
    slovo = mapa[x][y]
    if slovo == "E":
        slovo = "z"
    if ord(slovo) - ord(parent.letter) > 1:
        return
    if [x, y] in visited:
        return
    dist = parent.dist + 1
    p = Cell(x, y, mapa[x][y], 10000, None)
    if dist < p.dist :
        p.dist = dist
        #print("dodato u q", x, y)
        visited.append([p.x, p.y])
        queue.append(p)


with open(filename) as file:
    for line in file:
        row = line.rstrip()
        mapa.append([])
        for l in row:
            mapa[cnt_rows].append(l)
        #mapa.append(row)
        if "S" in row or "E" in row or "a" in row:
            found_s = False
            found_e = False
            for i in range(len(row)):
                if row[i] == "S" and not found_s:
                    location_S.append(cnt_rows)
                    location_S.append(i)
                    found_s = True
                if row[i] == "E" and not found_e:
                    location_E.append(cnt_rows)
                    location_E.append(i)
                    found_e = True
                if row[i] == "a":
                    all_a_letters.append([cnt_rows, i])

        cnt_rows += 1

#print(mapa)
#print("lokacija S:", location_S)
#print("lokacija E:", location_E)
minimal = BFS()
broj = len(all_a_letters)
for i, a in enumerate(all_a_letters):
    print("idemo na iduc", i, "/", broj)
    visited=[]
    queue = []
    mapa[location_S[0]][location_S[1]] = "a"
    mapa[a[0]][a[1]] = "S"
    location_S[0] = a[0]
    location_S[1] = a[1]
    #print(mapa)
    #print("lokacija S:", location_S)
    #print("lokacija E:", location_E)
    dulj = BFS()
    if dulj < minimal:
        minimal = dulj
print("RJESENJE", minimal)