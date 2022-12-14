filename = "input.txt"
array_of_cycles = [20, 60, 100, 140, 180, 220]
with open(filename) as file:
    num_of_cycles = 0
    value = 1
    total = 0
    for line in file:
        row = line.rstrip().split(" ")
        #print(num_of_cycles)
        #print("a komanda tu je ", row, "a vrijednost:", value)
        
        if len(row) == 1:
            
            num_of_cycles += 1
            if num_of_cycles in array_of_cycles:
                total += value*num_of_cycles
                print(num_of_cycles, ": ", value*num_of_cycles)
            
        else:
            num_of_cycles += 1
            if num_of_cycles in array_of_cycles:
                total += value*num_of_cycles
                print(num_of_cycles, ": ", value*num_of_cycles)
            num_of_cycles+= 1
            if num_of_cycles in array_of_cycles:
                total += value*num_of_cycles
                print(num_of_cycles, ": ", value*num_of_cycles)
            value += int(row[1])
print("TOTAL:", total)
