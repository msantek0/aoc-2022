filename = "input.txt"
import heapq
from functools import cmp_to_key

i = 0

class Signal:
    def __init__(self, s):
        self.s = s
    def __lt__(self, other):
        return usporedi(self.s, other.s) == -1


def create(array):
    global i
    arr = []
    if array[i] != '[' : raise Exception("Nije moguce da se ovo desi")
    i += 1
    while array[i] != ']':
        if array[i] == ',': 
            i = i + 1
            continue
        if array[i] == '[':
            arr.append([create(array)][0])
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
    #print("Dok python smatra:", len(left), "a len od right", len(right))
    for j in range(len(left)):
        if j >= len(right): return 1
        if type(left[j]) == list:
            if type(right[j]) == list:
                res = usporedi(left[j], right[j])
                if res != 0: return res
            else:
                res = usporedi(left[j], [right[j]])
                if res != 0: return res
        elif type(right[j]) == list:
            res = usporedi([left[j]], right[j])
            if res != 0: return res
        elif left[j] > right[j]: return 1
        elif left[j] < right[j]: return -1
    if len(left) == len(right):
        return 0
    return -1




all_signals_my = []
        
with open(filename) as file:
    cnt = 0
    left = []
    right = []
    total = 0
    idx_of_comp = 0
    for line in file:
        row = line.rstrip()
        if len(row) == 0:
            idx_of_comp += 1
            if usporedi(left, right) == -1:
                total += idx_of_comp
            continue
        if cnt == 0:
            cnt += 1
            left = create(row)
            all_signals_my.append(left)
            i = 0
        else:
            right = create(row)
            all_signals_my.append(right)
            i = 0
            cnt = 0
            


print("Total =", total)



all_signals_my.append([[2]])
all_signals_my.append([[6]])
switch_happen = True
while switch_happen:
    switch_happen = False
    for i in range(len(all_signals_my)-1):
        if usporedi(all_signals_my[i], all_signals_my[i+1]) == 1:
            tmp = all_signals_my[i]
            all_signals_my[i] = all_signals_my[i+1]
            all_signals_my[i+1] = tmp
            switch_happen = True
a = all_signals_my.index([[2]])-1
b = all_signals_my.index([[6]])-1
print("index", a)
print("index", b)

print("Rjesenje drugog dijela:", a*b)

            
