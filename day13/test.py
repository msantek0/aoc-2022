def create_array(depth):
    if depth == 1:
        return []
    return [create_array(depth-1)]


print(create_array(1))

def count_lenght(array, j):
    if array[j] != '[': return 0
    j = j+1
    s = ['[']
    cnt = 0
    while len(s) > 0:
        j = j+1
        if array[j-1] == '[': 
            s.append('[') 
        if array[j-1] == ']': 
            s.pop() 
        cnt += 1
        print("treunto brojim", array[j-1])
    return cnt

def create(array, i, duljina):
    if len(array) >= i: 
        return ""
    arr = []
    if array[i] == '[' : i = i+1
    for j in range(i, len(array)):
        if array[j] == ',': continue
        if array[j] == '[':
            #while array[j] != ']': 
            #    j = j+1
            arr.append([create(array, j+1, count_length(array, j))])
            
        arr.append(array[j])
    return arr
i = 0
def create1(array):
    global i
    arr = []
    if array[i] != '[' : raise Exception("Nije moguce da se ovo desi")
    i += 1
    while array[i] != ']':
        if array[i] == ',': 
            i = i + 1
            continue
        if array[i] == '[':
            arr.append([create1(array)][0])
        else:
            granica = i
            while array[i].isnumeric(): i = i+1
            arr.append(int(array[granica:i]))
            i = i-1
        i = i+1
        if len(array) < i:
            break
    return arr


def usporedi(left, right): 
    print("Left:", left)
    print("Right:", right)
    #print("Dok python smatra:", len(left), "a len od right", len(right))
    for j in range(0,len(left)):
        if j >= len(right): return 1
        if type(left[j]) == list:
            if type(right[j]) == list:
                res = usporedi(left[j], right[j])
                if res != -2: return res
            else:
                res = usporedi(left[j], [right[j]])
                if res != -2: return res
        elif type(right[j]) == list:
            res = usporedi([left[j]], right[j])
            if res != -2: return res
        elif left[j] > right[j]: return 1
        elif left[j] < right[j]: return -1
    print("doso sam tu")
    if len(left) == len(right):
        print("i vracam ovo")
        return -2
    return -1



test = "[[[[2],9,1,[2,2,4,8]],[1,8,8],9,[7,2,[7,0,1],0,[10,9,10,3]]]]"
test1 = "[1,1,3,1,1]"
test_r = "[1,1,5,1,1]"
test2 = "[[3,2],[4,8]]"
test3 = "[[[[3],10,0,[6,6,2,10],0],[4,[],[8,1,3,3],[10,4,10]]],[[],3,[0,[],[10,8,9,5,3],8,1]],[9,[]]]"
test4 = "[1,[2,[3,[4,[5,6,7]]]],8,9]"


#print("Pravi test", create1(test2))
i = 0
left = create1(test2)
i = 0
right = create1(test3)
print(usporedi(left, right))

