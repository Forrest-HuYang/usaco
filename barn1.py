"""
ID: tony_hu1
PROG: barn1
LANG: PYTHON3
"""
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def barn1_main(filein):
    plan = filein[0].split(' ')
    quantity = int(plan[0])
    total_length = int(plan[1])
    tbd = int(plan[2])
    filled = []
    for i in range(1,tbd+1):
        filled.append(int(filein[i]))
    filled.sort()
    if quantity >= tbd:
        quantity=tbd
    return total_length - greedy(quantity,total_length,tbd,filled)

def greedy(quantity,total_length,tbd,filled):
    difference_index = []
    for i in range(tbd-1):
        difference_index.append(filled[i+1]-filled[i]-1)
    print(difference_index)
    difference_index.sort()
    interval = 0
    for i in range(tbd-2,tbd-1-quantity,-1):
        interval += difference_index[i]
    interval += filled[0]-1 + total_length-filled[tbd-1]
    return interval
    



def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring)+'\n')

write_out('barn1.out',barn1_main(read_in('barn1.in')))