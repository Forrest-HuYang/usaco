def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def main(filein):
    no_box = int(filein[0])
    boxes = filein[1]
    return test(boxes)

def test(a):
    f = list(a)
    new = ''
    for y in range(len(f)-1):
        new += f[y+1]
    for i in range(len(a)):
        if i == len(a)-1:
            return len(a)
        m = ''
        for j in range(i+1):
            m += f[j]
        if not m in new:
            return i+1
        
def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring)+'\n')

write_out('whereami.out',main(read_in('whereami.in')))