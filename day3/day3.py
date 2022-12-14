help = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
worth = dict()
counter = 1
for letter in help:
    worth[letter] = counter
    counter += 1
filename = "input.txt"
with open(filename) as file:
    total = 0
    for line in file:
        first_half = line.rstrip()[:int(len(line.rstrip())/2)]
        second_half = line.rstrip()[int(len(line.rstrip())/2):]
        for letter in first_half:
            if letter in second_half:
                total += worth[letter]
                break

print(total)

filename = "input.txt"
with open(filename) as file:
    total = 0
    line1 = ""
    line2 = ""
    line3 = ""
    cnt = 0
    for i, line in enumerate(file):
        line1 = line.rstrip()
        cnt += 1
        if cnt%3==0:
            for letter in line1:
                if letter in line2 and letter in line3:
                    total += worth[letter]
                    break
        line3 = line2
        line2 = line1

print(total)