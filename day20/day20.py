filename = "input.txt"


def solve(length, arr, arr_length):
    for kan in range(length):
        for i in range(arr_length):
            if arr[i][1] == 0: continue
            old_position = arr[i][0]
            new_postition = (old_position + arr[i][1]) % (len_of_array-1)

            arr[i][0] = new_postition
            if old_position < new_postition:
                for j in range(len_of_array):
                    if j == i: continue
                    if arr[j][0] >= old_position and arr[j][0] <= new_postition:
                        arr[j][0] -= 1
            else:
                for j in range(len_of_array):
                    if j == i: continue
                    if arr[j][0] <= old_position and arr[j][0] >= new_postition:
                        arr[j][0] += 1
    idx = -1
    for i in arr:
        if i[1] == 0: 
            idx = i[0]
    return idx, arr

part_one_array = []
part_two_array = []
decription = 811589153
with open(filename) as file:
    part_one_array = [[idx, int(x)] for idx, x in enumerate(file.read().split("\n"))]

for i in part_one_array:
    part_two_array.append([i[0], i[1] * decription])

len_of_array = len(part_one_array)

idx_1, first_array = solve(1, part_one_array, len_of_array)
idx_2, second_array = solve(10, part_two_array, len_of_array)

first = [(idx_1+1000) % len_of_array, (idx_2+1000) % len_of_array,]
second = [(idx_1+2000) % len_of_array, (idx_2+2000) % len_of_array,]
third = [(idx_1+3000) % len_of_array, (idx_2+3000) % len_of_array,]


total1 = 0
for i in first_array:
    if i[0] in [first[0], second[0], third[0]]: 
        total1 += i[1]

total2 = 0
for i in second_array:
    if i[0] in [first[1], second[1], third[1]]: 
        total2 += i[1]


print("Part 1:", total1)
print("Part 2:", total2)