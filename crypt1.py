"""
ID: tony_hu1
PROG: crypt1
LANG: PYTHON3
"""
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def crypt1_main(filein):
    list_num = []
    list_initial = filein[1].split(' ')
    num_possible = int(filein[0])
    for i in range(num_possible):
        list_num.append(list_initial[i])
    if '0' in list_num:
        temp = list_num
        list_num.remove('0')
        possible_first_digit = list_num
        list_num = temp
    else:
        possible_first_digit = list_num
    return generate_nums(list_num,possible_first_digit,num_possible)


def generate_nums(list_num,possible_first_digit,num_possible):
    possible_first_num = []
    possible_second_num = []
    for i in range(len(possible_first_digit)):
        for j in range(num_possible):
            for k in range(num_possible):
                possible_first_num.append(int(possible_first_digit[i]+list_num[j]+list_num[k]))
    
    for x in range(len(possible_first_digit)):
        for y in range(num_possible):
            possible_second_num.append(int(possible_first_digit[x]+list_num[y]))
    
    return try_nums(possible_first_num,possible_second_num,list_num)

def try_nums(possible_first_num,possible_second_num,list_num):
    num_answers = 0
    for i in range(len(possible_first_num)):
        for j in range(len(possible_second_num)):
            if verify(possible_first_num,possible_second_num,i,j,list_num):
                num_answers += 1
    
    return num_answers


def verify(possible_first_num,possible_second_num,i,j,list_num):
    num1 = possible_first_num[i]
    num2 = possible_second_num[j]
    result_1 = num1*int(str(num2)[1])
    result_2 = num1*int(str(num2)[0])
    list_result1 = list(set(str(result_1)))
    a = len(list_result1)
    list_result2 = list(set(str(result_2)))
    b = len(list_result2)
    final_result = num1*num2
    list_final = list(set(str(final_result)))

    if result_1 >= 1000:
        return False

    for i in range(a):
        if not (list_result1[i] in list_num):
            return False

    if result_2 >= 10000:
        return False

    for i in range(b):
        if not (list_result2[i] in list_num):
            return False

    if final_result >= 10000:
        return False

    for i in range(len(list_final)):
        if not (list_final[i] in list_num):
            return False

    
    return True



def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring)+'\n')

write_out('crypt1.out',crypt1_main(read_in('crypt1.in')))