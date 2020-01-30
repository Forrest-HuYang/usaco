"""
ID: tony_hu1
PROG: ariprog
LANG: PYTHON3
"""
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def ariprog_main(filein):
    possible = []
    outstring = ''
    len_progression = int(filein[0])
    limit = int(filein[1])
    bisquare = listing_bisquares(limit)
    bisquare.sort()
    max = bisquare[len(bisquare)-1]
    for i in range(max+2-len_progression):
        if i in bisquare:
            jmax = (max-i)//(len_progression-1)+1
            for j in range(1,jmax+1):
                result = is_bisquare(i,j,bisquare,len_progression,max)
                if result == 2:
                    break
                elif result:
                    if not [j,i] in possible:
                        possible.append([j,i])
    if len(possible) == 0:
        return 'NONE'+'\n'
    possible.sort()
    print(possible)
    for k in range(len(possible)):
        outstring = outstring + str(possible[k][1]) + ' ' + str(possible[k][0]) + '\n'
    return outstring



def listing_bisquares(limit):
    bisquare = []
    for i in range(limit+1):
        for j in range(i,limit+1):
            bisquare.append(i**2 + j**2)
    return bisquare


def is_bisquare(a,b,bisquare,len_progression,max):
    current = a
    index = 0
    m = len(bisquare)
    for i in range(len_progression-1):
        current += b 
        if current > max:
            return 2
        if not current in bisquare[index:m+1]:
            return False
        index = bisquare.index(current)
    return True
        



def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(outstring)

write_out('ariprog.out',ariprog_main(read_in('ariprog.in')))