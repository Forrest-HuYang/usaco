import math
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def main(instring):
    is_on = False
    num_cows = int(instring[0])
    original = instring[1]
    current = instring[2]
    index = 0
    on_times = 0
    while index < num_cows:
        if current[index] == original[index]:
            index += 1
        else:
            is_on = True
            on_times += 1
        while is_on:
            index += 1
            if current[index] == original[index]:
                is_on = False

    fout = open('breedflip.out', 'w')
    fout.write(str(on_times) + '\n')


main(read_in('breedflip.in'))