cow_list = []
rotate_list = []
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def main(instring):
    global cow_list
    global rotate_list
    a = instring[0].split(' ')
    num_cows = int(a[0])
    num_rotates = int(a[1])
    num_times = int(a[2])
    temp_prev = 0
    for i in range(1,num_rotates+1):
        temp = instring[i].split(' ')
        if temp == temp_prev:
            rotate_list.pop()
            temp_prev = rotate_list[len(rotate_list)-1]
        else:
            a1 = int(temp[0])
            a2 = int(temp[1])
            rotate_list.append([a1,a2])

    remaining_times = 0
    cow_list = list(range(num_cows+1))
    list_original = cow_list[0:num_cows+1]
    

    for j in range(1,num_times+1):
        swap()
        if cow_list == list_original:
            remaining_times = num_times%j
            break

    if not remaining_times == 0:
        for k in range(remaining_times):
            swap()

    fout = open('swap.out', 'w')
    for k in range(1,num_cows+1):
        fout.write(str(cow_list[k]) + '\n')

def swap():
    global cow_list
    global rotate_list
    for i in rotate_list:
        a1 = i[0]
        a2 = i[1]
        target = cow_list[a1:a2+1]
        target.reverse()
        cow_list[a1:a2+1] = target
    

main(read_in('swap.in'))