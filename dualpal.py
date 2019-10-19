"""
ID: tony_hu1
PROG: dualpal
LANG: PYTHON3
"""
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def dualpal_main(filein):
    filein = filein[0].split(' ')
    out = ''
    num_needed = int(filein[0])
    num_init = int(filein[1])
    num_gotten = 0
    i = num_init+1
    while num_gotten < num_needed:
        if base_number(i):
            num_gotten += 1
            out = out + str(i) + '\n'
        i+=1
    return out

def base_number(num):
    original_num = num
    a = ''
    m = str(num)
    dual_score = 0
    for i in range(len(m)-1,-1,-1):
        a += m[i]
    if a == m:
        dual_score += 1

    for base in range(2,10):
        a = ''
        m = ''
        num = original_num
        while num > base:
            g = num % base
            a+=str(g)
            num = num // base
        if not num == 0:
            if num == base:
                a += '0'
                a += str(1)
            elif num < base:
                a += str(num)
        for j in range(len(a)-1,-1,-1):
            m += a[j]
        if m == a:
            dual_score+=1
        if dual_score == 2:
            return True
    return dual_score>= 2

def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring))

write_out('dualpal.out',dualpal_main(read_in('dualpal.in')))