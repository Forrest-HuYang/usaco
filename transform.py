"""
ID: tony_hu1
PROG: transform
LANG: PYTHON2
"""
import numpy as np
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a 

def transform_main(flines):
    square_side = int(flines[0])
    original_square = []
    new_square = []
    ors = []
    ns = []
    for i in range(1,square_side+1):
        original_square.append(list(flines[i]))
        ors += list(flines[i])
    for i in range(square_side+1,2*square_side+1):
        new_square.append(list(flines[i]))
        ns += list(flines[i])
        


    if ors.count('-') != ns.count('-'):
        return 7

    original_square = np.array(original_square)
    new_square = np.array(new_square)

    a = judgement(original_square,new_square)
    if type(a) == int:
        if a == 3:
            m = ninety_degrees(ninety_degrees(ninety_degrees(original_square))) == ninety_degrees(original_square)
            if m.all:
                return 1
        return a

    mirror = np.fliplr(original_square)
    x = (mirror == new_square)
    if x.all():
        return 4

    a = judgement(mirror,new_square)
    if type(a) == int:
        return 5
    
    m = (new_square == original_square)
    if m.all():
        return 6

    return 7

def judgement(original_square,new_square):
    for i in range(3):
        original_square = ninety_degrees(original_square)
        a = (original_square == new_square)
        if a.all():
            return 3-i

def ninety_degrees(array):
    temp = np.zeros_like(array.transpose())
    for j in range(len(array)):
        for i in range(len(array[0])):
            temp[i][j] = array[j][len(array[0])-i-1]
    return temp


def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring) + '\n')

write_out('transform.out',transform_main(read_in('transform.in')))