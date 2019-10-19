"""
ID: tony_hu1
PROG: palsquare
LANG: PYTHON3
"""
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a = int(line.rstrip())
    return a

def palsquare_main(base):
    out = ''
    for i in range(1,301):
        judgement = base_number(base,i**2)
        if judgement[0] == True:
            out = out + base_number(base,i)[1] + ' ' + judgement[1] + '\n'
    return out

def base_number(base,num):
    a = ''
    m = ''
    original = num
    over_10 = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J'}
    if base == 10:
        m = str(num)
        for i in range(len(m)-1,-1,-1):
            a += m[i]

    else:
        while num != base and not num == 0:
            g = num % base
            if base < 10 or g <10:
                a+=str(g)
            else:
                a+=over_10[g]
            num = num // base
        if not num == 0:
            if num == base:
                a += '0'
                a += str(1)
            if num < base:
                a += num
        for i in range(len(a)-1,-1,-1):
            m += a[i]
    return m==a,m

def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring))

write_out('palsquare.out',palsquare_main(read_in('palsquare.in')))