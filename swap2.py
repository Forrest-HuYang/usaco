import sys
sys.setrecursionlimit(1000000)
a1 = 0
a2 = 0
b1 = 0
b2 = 0
cow_list = []
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def main(instring):
    global a1
    global a2
    global b1
    global b2
    global cow_list
    a = instring[0].split(' ')
    num_cows = int(a[0])
    num_times = int(a[1])
    a = instring[1].split(' ')
    a1 = int(a[0])
    a2 = int(a[1])
    a = instring[2].split(' ')
    b1 = int(a[0])
    b2 = int(a[1])
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
    global a1
    global a2
    global b1
    global b2
    global cow_list
    target = cow_list[a1:a2+1]
    target.reverse()
    cow_list[a1:a2+1] = target
    target = cow_list[b1:b2+1]
    target.reverse()
    cow_list[b1:b2+1] = target

main(read_in('swap.in'))