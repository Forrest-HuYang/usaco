"""
ID: tony_hu1
PROG: combo
LANG: PYTHON3
"""
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def combo_main(filein):
    combo_farmer = []
    combo_master = []
    farmer = filein[1].split(' ')
    master = filein[2].split(' ')
    N = int(filein[0])
    for i in range(3):
        combo_farmer.append(int(farmer[i]))
        combo_master.append(int(master[i]))



    return listing(N,combo_farmer,combo_master)

def listing(N,combo_farmer,combo_master):
    farmer = []
    master = []
    possible = []
    for i in range(3):
        farmer.append(get_possible_digits(N,combo_farmer[i]))
        master.append(get_possible_digits(N,combo_master[i]))
    
    z = len(get_possible_digits(N,combo_farmer[i]))

    for i in range(z):
        for j in range(z):
            for k in range(z):
                m = [farmer[0][i],farmer[1][j],farmer[2][k]]
                n = [master[0][i],master[1][j],master[2][k]] 
                if not m in possible:
                    possible.append(m)
                if not n in possible:
                    possible.append(n)
    print(possible)
    

    return len(possible)

def get_possible_digits(N,number):
    if N == 1:
        return [1]
    if N == 2:
        return [1,2]
    if N == 3:
        return [1,2,3]
    if N == 4:
        return [1,2,3,4]
    if (number <= N - 2) and (number >= 3):
        m = [number-2,number-1,number,number+1,number+2]
        return m
    if number > N - 2:
        if number = N -1:
            return [N-3,N-2,N-1,N,1]
        else:
            return [N-2,N-1,N,1,2]
        n = [number-2,number-1,number,(number+2)%N,(number+3)%N]
        if 0 in n:
            n.remove(0)
        return n
    else:
        if number == 2:
            return [N,1,2,3,4]
        else:
            return [N-1,N,1,2,3]


def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring)+'\n')

write_out('combo.out',combo_main(read_in('combo.in')))