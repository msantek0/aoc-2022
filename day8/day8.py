filename = "input.txt"

trees = []
cnt = 0

def check_range(tree, x, start, end, row):
    global trees
    if row:
        for i in range(start, end):
            if trees[x][i] >= tree: return False
        return True
    for i in range(start, end):
        if trees[i][x] >= tree: return False
    return True

def visible(tree, x, y):
    global trees, cnt
    if tree == 0: return False
    if check_range(tree, x, 0, y, True): return True
    if check_range(tree, x, y+1, cnt, True): return True
    if check_range(tree, y, 0, x, False): return True
    if check_range(tree, y, x+1, cnt, False): return True
    return False

def num_of_visible_trees(tree, x, start, end, step, row):
    global trees
    counter = 0
    if row:
        for i in range(start, end, step):
            if trees[x][i] >= tree: 
                counter += 1
                return counter
            counter += 1
        return counter
    for i in range(start, end, step):
        if trees[i][x] >= tree: 
            counter += 1
            return counter
        counter += 1
    return counter


def calculate_ss(tree, x, y):
    global trees, cnt
    science_score = 1
    science_score *= num_of_visible_trees(tree, y, x-1, -1, -1, False)
    science_score *= num_of_visible_trees(tree, y, x+1, cnt, 1, False)
    science_score *= num_of_visible_trees(tree, x, y-1, -1, -1, True)
    science_score *= num_of_visible_trees(tree, x, y+1, cnt, 1, True)
    return science_score




with open(filename) as file:

    for line in file:
        trees.append([])
        for tree in line.rstrip():
            trees[cnt].append(tree)
        cnt+=1
#print(trees[1][2])

num_of_visible = 0
for i in range(1, cnt-1):
    for j in range(1, cnt-1):
        if visible(trees[i][j], i, j):
            num_of_visible += 1

num_of_visible += cnt*4 - 4
print("Broj vidljivih stabala:", num_of_visible)


max_scenic_score = 0

for i in range(1, cnt-1):
    for j in range(1, cnt-1):
        current_science_score = calculate_ss(trees[i][j], i, j)
        if current_science_score > max_scenic_score:
            max_scenic_score = current_science_score

print("Maksimalni scienc score:", max_scenic_score)
#print(trees[3][2], "Na poziiciji (3, 2) je:", calculate_ss(trees[3][2], 3, 2))
