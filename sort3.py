"""
ID: tony_hu1
PROG: sort3
LANG: PYTHON3
"""
def check_swap(current_num):
    global unsorted
    global sorted
    global num
    global steps
    global area

    for i in range(num):
        if sorted[i] > current_num:
            return
        if sorted[i] == current_num:
            if unsorted[i] == current_num:
                unsorted[i] = 0
            else:
                wrong_num = unsorted[i]
                area[1] = unsorted[0:count_1]
                area[2] = unsorted[count_1:count_1 + count_2]
                area[3]=  unsorted[count_1 + count_2 : num]
                if current_num in area[wrong_num]:
                    to_be_changed = area[wrong_num].index(current_num) + alterable[wrong_num-1]
                else:
                    to_be_changed = unsorted[alterable[current_num]:num].index(current_num) + alterable[current_num]
                unsorted[i],unsorted[to_be_changed] = 0,unsorted[i]
                steps += 1
sorted = []
with open('sort3.in') as filename:
    for line in filename:
        sorted.append(int(line.rstrip()))

num = sorted[0]
del sorted[0]
unsorted = sorted[0:num]
sorted.sort()
area = dict()
steps = 0
count_1 = sorted.count(1)
count_2 = sorted.count(2)
alterable = {1:count_1,2:count_1+count_2}

for i in range(1,3):
    check_swap(i)





fout = open('sort3.out', 'w')
fout.write(str(steps)+'\n')



