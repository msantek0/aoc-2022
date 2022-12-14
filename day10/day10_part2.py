filename = "input.txt"
array_of_cycles = [20, 60, 100, 140, 180, 220]
position_of_sprite = [0,1,2]
drawing = []
num_of_cycles = 0

def draw():
    global position_of_sprite, drawing, num_of_cycles
    print("crtam na poziciji:", num_of_cycles, "dok je", position_of_sprite)
    if num_of_cycles % 40 in position_of_sprite:
        drawing.append("#")
    else:
        drawing.append(".")

with open(filename) as file:
    for line in file:
        row = line.rstrip().split(" ")
        #print(num_of_cycles)
        #print("a komanda tu je ", row, "a vrijednost:", value)
        
        if len(row) == 1:
            draw()
            num_of_cycles += 1
            
        else:
            draw()
            num_of_cycles += 1
            draw()
            num_of_cycles+= 1
            position_of_sprite = [i + int(row[1]) for i in position_of_sprite]
            print("NOVA POZICIJA:", position_of_sprite)

print()
print()
print()
for i in range(6):
    for j in range(40):
        print(drawing[i*40+j], end="")
    print()
