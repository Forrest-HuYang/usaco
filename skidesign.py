"""
ID: tony_hu1
PROG: skidesign
LANG: PYTHON3
"""
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def skidesign_main(filein):
    no_hills = int(filein[0])
    height = []
    for i in range(1,no_hills+1):
        height.append(int(filein[i]))
    height.sort()
    return greedy(height,no_hills)
        
def greedy(height,no_hills):
    lowest = height[0]
    highest = height[no_hills-1]
    total = []
    if highest-lowest <= 17:
        return 0
    for i in range(lowest,highest-16):
        low = i
        hi = i+17
        sum = 0
        for j in range(no_hills):
            current = height[j]
            if current < low:
                sum += (low-current)**2
            elif current > hi:
                sum += (current-hi)**2
        total.append(sum)
    return min(total)
                


def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring)+'\n')

write_out('skidesign.out',skidesign_main(read_in('skidesign.in')))
