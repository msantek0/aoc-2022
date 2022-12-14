filename = "input.txt"
with open(filename) as file:
    max_callories = 0
    second_max = 0
    third_max = 0
    current = 0
    for line in file:
        row = line.rstrip()
        if row == "":
            if current > max_callories:
                third_max = second_max
                second_max = max_callories
                max_callories = current
            elif current > second_max:
                third_max = second_max
                second_max = current
            elif current > third_max:
                third_max = current
            current = 0
        else:
            current += int(row)
    if current > max_callories:
        third_max = second_max
        second_max = max_callories
        max_callories = current
    elif current > second_max:
        third_max = second_max
        second_max = current
    elif current > third_max:
        third_max = current
    
print(max_callories + second_max + third_max)

        
            