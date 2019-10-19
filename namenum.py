"""
ID: tony_hu1
PROG: namenum
LANG: PYTHON3
"""
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a 

def name_main(num,dicts):
    m = []
    out = ''
    length = len(num[0])
    n = {'2': ['A','B','C'],'5': ['J','K','L'],'8': ['T','U','V'],'3': ['D','E','F'],'6': ['M','N','O'],'9': ['W','X','Y'],'4': ['G','H','I'],'7': ['P','R','S']}
    for i in range(len(dicts)):
        h = dicts[i]
        if len(h) == length:
            if is_name(length,h,n,num):
                out = out + h + '\n'
    if out == '':
        out = out + 'NONE' + '\n'
    return out

def is_name(length,h,n,num):
    for j in range(length):
        if not (h[j] in n[num[0][j]]):
            return False
    return True

def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring))


write_out('namenum.out',name_main(read_in('namenum.in'),read_in('dict.txt')))